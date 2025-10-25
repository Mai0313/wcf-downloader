<div align="center" markdown="1">

# HCFDownloader (戶晨風下載器)

[![PyPI version](https://img.shields.io/pypi/v/hcf-downloader.svg)](https://pypi.org/project/hcf-downloader/)
[![python](https://img.shields.io/badge/-Python_%7C_3.11%7C_3.12%7C_3.13%7C_3.14-blue?logo=python&logoColor=white)](https://www.python.org/downloads/source/)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
[![tests](https://github.com/Mai0313/hcf_downloader/actions/workflows/test.yml/badge.svg)](https://github.com/Mai0313/hcf_downloader/actions/workflows/test.yml)
[![code-quality](https://github.com/Mai0313/hcf_downloader/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/Mai0313/hcf_downloader/actions/workflows/code-quality-check.yml)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/Mai0313/hcf_downloader/tree/main?tab=License-1-ov-file)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mai0313/hcf_downloader/pulls)
[![contributors](https://img.shields.io/github/contributors/Mai0313/hcf_downloader.svg)](https://github.com/Mai0313/hcf_downloader/graphs/contributors)

</div>

🎥 A specialized YouTube channel downloader for archiving 戶晨風 (HCF) streams and videos. Download entire channels or individual videos with ease.

Other Languages: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## ✨ Features

- 🎬 **YouTube Channel Downloader**: Download all videos from 戶晨風's YouTube channel
- 🔄 **High Quality Downloads**: Support for multiple quality options (best, high, medium, low)
- 📦 **Modern Python Stack**: Built with Pydantic, yt-dlp, and Rich for robust functionality
- 🎯 **Simple CLI**: Easy-to-use command-line interface powered by Python Fire
- 🔁 **Retry Mechanism**: Automatic retries for failed downloads
- 📁 **Organized Output**: Videos saved to customizable download folders
- 🎨 **Rich Progress Display**: Beautiful terminal output with Rich library
- 🌐 **Multi-site Support**: Works with YouTube, Bilibili, and other video platforms

## 🚀 Quick Start

### Prerequisites

- Python 3.11–3.14
- `uv` (install with `make uv-install`)

### Installation

```bash
# Install uv (if not already installed)
make uv-install

# Install dependencies
uv sync
```

### Basic Usage

Download a single video:

```bash
# Download with default settings (best quality)
uv run hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID"

# Specify quality
uv run hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID" --quality="high"
```

Or use the CLI entry point:

```bash
# After installation
hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID"
```

### Advanced Usage

```python
from hcf_downloader.cli import VideoDownloader

# Initialize downloader
downloader = VideoDownloader(output_folder="./my_downloads", max_retries=5)

# Download a video
title, filepath = downloader.download(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    quality="best",  # Options: best, high, medium, low
)

print(f"Downloaded: {title} to {filepath}")
```

## 🧰 Commands Reference

```bash
# Development
make help               # List available make targets
make clean              # Clean caches and artifacts
make format             # Run all pre-commit hooks
make test               # Run pytest

# Dependencies (via uv)
make uv-install         # Install uv on your system
uv add <pkg>            # Add production dependency
uv sync                 # Install all dependencies
```

## 📝 Quality Settings

HCFDownloader supports multiple quality presets:

- **best**: Best available video and audio quality (default)
- **high**: Up to 1080p at 60fps
- **medium**: Up to 720p at 60fps
- **low**: Up to 480p

## 🛠️ Development

### Setting up development environment

```bash
# Install development dependencies
uv sync --group dev

# Install pre-commit hooks
uv tool install pre-commit
make format

# Run tests
make test
```

## 📦 Project Structure

```
hcf_downloader/
├── src/
│   └── hcf_downloader/
│       ├── __init__.py
│       └── cli.py          # Main CLI and downloader logic
├── tests/
│   └── test_hello.py
├── pyproject.toml          # Project configuration
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp) for robust video downloading
- Uses [Pydantic](https://docs.pydantic.dev/) for data validation
- Terminal UI powered by [Rich](https://github.com/Textualize/rich)
- CLI interface via [Python Fire](https://github.com/google/python-fire)

---

<div align="center">
Made with ❤️ for archiving 戶晨風's content
</div>
uv add <pkg> --dev      # Add development dependency
```

## 🎯 About HCF (戶晨風)

This tool is specifically designed to archive content from 戶晨風's YouTube channel. It supports downloading:

- Live streams
- Regular videos
- Entire channel archives

## ⚙️ Configuration

You can customize the downloader behavior:

```python
from hcf_downloader.cli import VideoDownloader

downloader = VideoDownloader(
    output_folder="./my_custom_folder",  # Custom download location
    max_retries=10,  # Increase retry attempts
)
```

## � Technical Details

Built with modern Python best practices:

- Type-hinted code with Pydantic models
- Robust error handling and retry mechanisms
- Beautiful terminal output with Rich
- Configurable quality settings
- Support for multiple video platforms
  - Builds multi-platform executables (via PyInstaller):
    - macOS (ARM64, x64)
    - Linux (x64 GNU, ARM64 GNU)
    - Windows (x64, ARM64)
  - Builds Python package (wheel & sdist)
  - Automatically publishes to PyPI (requires `UV_PUBLISH_TOKEN` secret)
  - Uploads all artifacts to GitHub Release

## 📚 Documentation

For more detailed information:

- Check out the [project homepage](https://mai0313.github.io/hcf_downloader)
- Visit the [GitHub repository](https://github.com/Mai0313/hcf_downloader)

## ❓ FAQ

**Q: Can I download playlists?**
A: Currently, the tool is set to download individual videos. Playlist support may be added in future versions.

**Q: What video formats are supported?**
A: The tool outputs MP4 files by default, which are compatible with most media players.

**Q: How do I stop a download?**
A: Press `Ctrl+C` to cancel the current download.

**Q: Can I use this for other YouTube channels?**
A: Yes! While designed for 戶晨風's channel, this tool works with any YouTube video or channel.
