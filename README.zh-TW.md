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

🎥 專為存檔戶晨風（HCF）直播和影片而設計的 YouTube 頻道下載工具。輕鬆下載整個頻道或單個影片。

其他語言: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## ✨ 功能特點

- 🎬 **YouTube 頻道下載器**：下載戶晨風 YouTube 頻道的所有影片
- 🔄 **高品質下載**：支援多種品質選項（最佳、高清、中等、低）
- 📦 **現代 Python 技術棧**：使用 Pydantic、yt-dlp 和 Rich 建構，功能強大
- 🎯 **簡單 CLI**：基於 Python Fire 的易用命令列介面
- 🔁 **重試機制**：下載失敗自動重試
- 📁 **有序輸出**：影片儲存到可自訂的下載資料夾
- 🎨 **豐富進度顯示**：使用 Rich 函式庫提供精美的終端輸出
- 🌐 **多站點支援**：支援 YouTube、Bilibili 等影片平台

## 🚀 快速開始

### 前置要求

- Python 3.11–3.14
- `uv`（使用 `make uv-install` 安裝）

### 安裝

```bash
# 安裝 uv（如果尚未安裝）
make uv-install

# 安裝依賴
uv sync
```

### 基本使用

下載單個影片：

```bash
# 使用預設設定下載（最佳品質）
uv run hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID"

# 指定品質
uv run hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID" --quality="high"
```

或使用 CLI 入口點：

```bash
# 安裝後
hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID"
```

### 進階使用

```python
from hcf_downloader.cli import VideoDownloader

# 初始化下載器
downloader = VideoDownloader(output_folder="./my_downloads", max_retries=5)

# 下載影片
title, filepath = downloader.download(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    quality="best",  # 選項：best、high、medium、low
)

print(f"已下載：{title} 到 {filepath}")
```

## 🧰 指令參考

```bash
# 開發
make help               # 顯示可用的 make 指令
make clean              # 清理快取和產物
make format             # 執行所有 pre-commit hooks
make test               # 執行 pytest

# 依賴管理（uv）
make uv-install         # 安裝 uv
uv add <pkg>            # 加入正式依賴
uv sync                 # 安裝所有依賴
uv add <pkg> --dev      # 加入開發依賴
```

## 📝 品質設定

HCFDownloader 支援多種品質預設：

- **best**：最佳影片和音訊品質（預設）
- **high**：最高 1080p @ 60fps
- **medium**：最高 720p @ 60fps
- **low**：最高 480p

## 🎯 關於 HCF（戶晨風）

此工具專門用於存檔戶晨風 YouTube 頻道的內容。支援下載：

- 直播回放
- 常規影片
- 整個頻道存檔

## ⚙️ 設定

您可以自訂下載器行為：

```python
from hcf_downloader.cli import VideoDownloader

downloader = VideoDownloader(
    output_folder="./my_custom_folder",  # 自訂下載位置
    max_retries=10,  # 增加重試次數
)
```

## 🛠️ 開發

### 設定開發環境

```bash
# 安裝開發依賴
uv sync --group dev

# 安裝 pre-commit hooks
uv tool install pre-commit
make format

# 執行測試
make test
```

## 📦 專案結構

```
hcf_downloader/
├── src/
│   └── hcf_downloader/
│       ├── __init__.py
│       └── cli.py          # 主 CLI 和下載器邏輯
├── tests/
│   └── test_hello.py
├── pyproject.toml          # 專案設定
└── README.md
```

## 🔧 技術細節

使用現代 Python 最佳實踐建構：

- 使用 Pydantic 模型的型別註解程式碼
- 強大的錯誤處理和重試機制
- 使用 Rich 提供精美的終端輸出
- 可設定的品質設定
- 支援多個影片平台

## 📚 文件

更多詳細資訊：

- 查看[專案首頁](https://mai0313.github.io/hcf_downloader)
- 造訪 [GitHub 倉庫](https://github.com/Mai0313/hcf_downloader)

## ❓ 常見問題

**問：可以下載播放清單嗎？**
答：目前工具設定為下載單個影片。播放清單支援可能會在未來版本中新增。

**問：支援哪些影片格式？**
答：工具預設輸出 MP4 檔案，相容大多數媒體播放器。

**問：如何停止下載？**
答：按 `Ctrl+C` 取消目前下載。

**問：可以用於其他 YouTube 頻道嗎？**
答：可以！雖然是為戶晨風頻道設計的，但此工具適用於任何 YouTube 影片或頻道。

## 🤝 貢獻

歡迎貢獻！請隨時提交 Pull Request。

## 📄 授權

本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。

## 🙏 致謝

- 使用 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 實現強大的影片下載
- 使用 [Pydantic](https://docs.pydantic.dev/) 進行資料驗證
- 使用 [Rich](https://github.com/Textualize/rich) 提供終端 UI
- 使用 [Python Fire](https://github.com/google/python-fire) 提供 CLI 介面

---

<div align="center">
用 ❤️ 為存檔戶晨風的內容而製作
</div>

- 發佈到 PyPI 後，透過 `uvx`（臨時安裝後執行）：

```bash
# 若 console script 名稱為 "hcf_downloader"
uvx hcf_downloader

# 或指定套件/版本與入口名稱
uvx --from your-package-name==0.1.0 your-entrypoint
```

## 🧭 選用任務管理（Poe the Poet）

`pyproject.toml` 中的 `[tool.poe.tasks]` 定義了便捷任務，安裝 dev 群組（`uv sync --group dev`）或使用 `uvx` 後可用：

```bash
uv run poe docs        # 生成 + 啟動文件預覽（需 dev 群組）
uv run poe gen         # 生成 + 發佈文件（gh-deploy）（需 dev 群組）
uv run poe main        # 執行 CLI（等同 uv run hcf_downloader）

# 或使用 uvx（臨時環境，無需本地安裝）
uvx poe docs
```

## 🔁 CI/CD 工作流程總覽

所有流程位於 `.github/workflows/`，以下為觸發時機與用途：

- Tests（`test.yml`）

  - 觸發：對 `main`、`release/*` 的 PR
  - 執行 pytest（3.11/3.12/3.13/3.14）並留下覆蓋率摘要

- Code Quality（`code-quality-check.yml`）

  - 觸發：PR
  - 執行 ruff 與其它 pre-commit hooks

- Docs Deploy（`deploy.yml`）

  - 觸發：推送到 `main` 與 `v*` 標籤
  - 建置並發布 MkDocs 網站到 GitHub Pages
  - 需在 GitHub 啟用 Pages（Actions → Pages）

- Build and Release（`build_release.yml`）

  - 觸發：`v*` 標籤推送或手動觸發
  - 建置多平台可執行檔（透過 PyInstaller）：
    - macOS（ARM64、x64）
    - Linux（x64 GNU、ARM64 GNU）
    - Windows（x64、ARM64）
  - 建置 Python 套件（wheel & sdist）
  - 自動發布到 PyPI（需設定 `UV_PUBLISH_TOKEN` secret）
  - 上傳所有產物至 GitHub Release
  - 注意：此為 template 示範流程，請依實際專案需求調整

- Publish Docker Image（`build_image.yml`）

  - 觸發：推送到 `main` 與 `v*` 標籤
  - 發佈至 GHCR：`ghcr.io/<owner>/<repo>`（需 `docker/Dockerfile` 內有 `prod` target）

- Release Drafter（`release_drafter.yml`）

  - 觸發：推送到 `main` 與 PR 事件
  - 基於 Conventional Commits 維護草稿發佈

- PR Labeler（`auto_labeler.yml`）

  - 觸發：PR 與 Push
  - 依 `.github/labeler.yml` 自動加標籤

- Secret Scanning（`secret_scan.yml`）

  - 觸發：Push 與 PR
  - 使用 gitleaks 掃描機密

- Semantic Pull Request（`semantic-pull-request.yml`）

  - 觸發：PR 開啟/更新
  - 強制 PR 標題符合 Conventional Commits

### CI/CD 設定清單

- PR 標題遵循 Conventional Commits
- （選用）發佈到 PyPI：在 repository 設定中新增 `UV_PUBLISH_TOKEN` secret（Settings → Secrets and variables → Actions）
- （選用）啟用 GitHub Pages 以發布文件（Settings → Pages → Source: GitHub Actions）
- （選用）發佈 Docker 映像檔：確認 GHCR 權限已啟用（Settings → Actions → General → Workflow permissions: Read and write）

## 🧩 範例 CLI

`pyproject.toml` 內提供 `hcf_downloader` 與 `cli` 兩個入口點。目前示範回傳簡單 `Response` 模型，可依需求替換。

```bash
uv run hcf_downloader
```

## 🤝 貢獻

- 歡迎 Issue/PR
- 請遵循程式風格（ruff、型別）
- PR 標題遵循 Conventional Commits

## 📄 授權

MIT — 詳見 `LICENSE`。
