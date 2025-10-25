from typing import Any
from pathlib import Path
from functools import cached_property

import fire
from yt_dlp import YoutubeDL
from pydantic import Field, BaseModel, computed_field
from rich.console import Console

console = Console()


class VideoDownloader(BaseModel):
    output_folder: str = Field(default="./downloads", description="Download folder")
    max_retries: int = Field(default=5)

    @computed_field
    @cached_property
    def quality_formats(self) -> dict[str, str]:
        quality_formats = {
            "best": "bestvideo*+bestaudio/best/bestvideo*",
            "high": "bestvideo[height<=1080][fps<=60]+bestaudio/best[height<=1080][fps<=60]/best[height<=1080]",
            "medium": "bestvideo[height<=720][fps<=60]+bestaudio/best[height<=720][fps<=60]/best[height<=720]",
            "low": "bestvideo[height<=480]+bestaudio/best[height<=480]/best[height<=480]",
        }
        return quality_formats

    def get_params(self, quality: str, url: str) -> dict[str, Any]:
        output_path = Path(self.output_folder)
        output_path.mkdir(parents=True, exist_ok=True)

        # Base headers safe for most sites; site-specific headers added conditionally below
        http_headers: dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        }
        if "bilibili.com" in url:
            http_headers["Referer"] = "https://www.bilibili.com"

        params = {
            "format": self.quality_formats.get(quality, "best"),
            "outtmpl": f"{output_path.as_posix()}/%(title)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "continuedl": True,
            "noplaylist": True,
            "restrictfilenames": True,
            "writeinfojson": False,
            "writedescription": False,
            "writesubtitles": False,
            "writeautomaticsub": False,
            "ignoreerrors": False,
            "retries": 3,
            "fragment_retries": 3,
            "merge_output_format": "mp4",
            "http_headers": http_headers,
            "socket_timeout": 30,
            "extractor_retries": 3,
            "geo_bypass": True,
        }
        return params

    def download(self, url: str, quality: str = "best") -> tuple[str, Path]:
        params = self.get_params(quality=quality, url=url)
        with YoutubeDL(params=params) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "")
            filename = Path(ydl.prepare_filename(info))
            console.print(f"[green]Downloaded:[/green] {title} -> {filename.as_posix()}")
            return title, filename


def main(url: str = "https://www.youtube.com/watch?v=4sDXl73ECAo") -> None:
    downloader = VideoDownloader()
    downloader.download(url=url, quality="best")


def entry() -> None:
    fire.Fire(main)


if __name__ == "__main__":
    entry()
