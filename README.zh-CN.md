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

🎥 专为存档戶晨風（HCF）直播和视频而设计的 YouTube 频道下载工具。轻松下载整个频道或单个视频。

其他语言: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## ✨ 功能特点

- 🎬 **YouTube 频道下载器**：下载戶晨風 YouTube 频道的所有视频
- 🔄 **高质量下载**：支持多种质量选项（最佳、高清、中等、低）
- 📦 **现代 Python 技术栈**：使用 Pydantic、yt-dlp 和 Rich 构建，功能强大
- 🎯 **简单 CLI**：基于 Python Fire 的易用命令行界面
- 🔁 **重试机制**：下载失败自动重试
- 📁 **有序输出**：视频保存到可自定义的下载文件夹
- 🎨 **丰富进度显示**：使用 Rich 库提供精美的终端输出
- 🌐 **多站点支持**：支持 YouTube、Bilibili 等视频平台

## 🚀 快速开始

### 前置要求

- Python 3.11–3.14
- `uv`（使用 `make uv-install` 安装）

### 安装

```bash
# 安装 uv（如果尚未安装）
make uv-install

# 安装依赖
uv sync
```

### 基本使用

下载单个视频：

```bash
# 使用默认设置下载（最佳质量）
uv run hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID"

# 指定质量
uv run hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID" --quality="high"
```

或使用 CLI 入口点：

```bash
# 安装后
hcf_downloader --url="https://www.youtube.com/watch?v=VIDEO_ID"
```

### 高级使用

```python
from hcf_downloader.cli import VideoDownloader

# 初始化下载器
downloader = VideoDownloader(output_folder="./my_downloads", max_retries=5)

# 下载视频
title, filepath = downloader.download(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    quality="best",  # 选项：best、high、medium、low
)

print(f"已下载：{title} 到 {filepath}")
```

## 🧰 命令参考

```bash
# 开发
make help               # 显示可用的 make 命令
make clean              # 清理缓存和产物
make format             # 运行所有 pre-commit hooks
make test               # 运行 pytest

# 依赖管理（uv）
make uv-install         # 安装 uv
uv add <pkg>            # 添加生产依赖
uv sync                 # 安装所有依赖
uv add <pkg> --dev      # 添加开发依赖
```

## 📝 质量设置

HCFDownloader 支持多种质量预设：

- **best**：最佳视频和音频质量（默认）
- **high**：最高 1080p @ 60fps
- **medium**：最高 720p @ 60fps
- **low**：最高 480p

## 🎯 关于 HCF（戶晨風）

此工具专门用于存档戶晨風 YouTube 频道的内容。支持下载：

- 直播回放
- 常规视频
- 整个频道存档

## ⚙️ 配置

您可以自定义下载器行为：

```python
from hcf_downloader.cli import VideoDownloader

downloader = VideoDownloader(
    output_folder="./my_custom_folder",  # 自定义下载位置
    max_retries=10,  # 增加重试次数
)
```

## 🛠️ 开发

### 设置开发环境

```bash
# 安装开发依赖
uv sync --group dev

# 安装 pre-commit hooks
uv tool install pre-commit
make format

# 运行测试
make test
```

## 📦 项目结构

```
hcf_downloader/
├── src/
│   └── hcf_downloader/
│       ├── __init__.py
│       └── cli.py          # 主 CLI 和下载器逻辑
├── tests/
│   └── test_hello.py
├── pyproject.toml          # 项目配置
└── README.md
```

## 🔧 技术细节

使用现代 Python 最佳实践构建：

- 使用 Pydantic 模型的类型注解代码
- 强大的错误处理和重试机制
- 使用 Rich 提供精美的终端输出
- 可配置的质量设置
- 支持多个视频平台

## 📚 文档

更多详细信息：

- 查看[项目主页](https://mai0313.github.io/hcf_downloader)
- 访问 [GitHub 仓库](https://github.com/Mai0313/hcf_downloader)

## ❓ 常见问题

**问：可以下载播放列表吗？**
答：目前工具设置为下载单个视频。播放列表支持可能会在未来版本中添加。

**问：支持哪些视频格式？**
答：工具默认输出 MP4 文件，兼容大多数媒体播放器。

**问：如何停止下载？**
答：按 `Ctrl+C` 取消当前下载。

**问：可以用于其他 YouTube 频道吗？**
答：可以！虽然是为戶晨風频道设计的，但此工具适用于任何 YouTube 视频或频道。

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 使用 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 实现强大的视频下载
- 使用 [Pydantic](https://docs.pydantic.dev/) 进行数据验证
- 使用 [Rich](https://github.com/Textualize/rich) 提供终端 UI
- 使用 [Python Fire](https://github.com/google/python-fire) 提供 CLI 界面

---

<div align="center">
用 ❤️ 为存档戶晨風的内容而制作
</div>

- 发布到 PyPI 后，通过 `uvx`（临时安装后执行）：

```bash
# 若 console script 名称为 "hcf_downloader"
uvx hcf_downloader

# 或指定包/版本与入口名称
uvx --from your-package-name==0.1.0 your-entrypoint
```

## 🧭 选用任务管理（Poe the Poet）

`pyproject.toml` 中的 `[tool.poe.tasks]` 定义了便捷任务，安装 dev 群组（`uv sync --group dev`）或使用 `uvx` 后可用：

```bash
uv run poe docs        # 生成 + 启动文档预览（需 dev 群组）
uv run poe gen         # 生成 + 发布文档（gh-deploy）（需 dev 群组）
uv run poe main        # 执行 CLI（等同 uv run hcf_downloader）

# 或使用 uvx（临时环境，无需本地安装）
uvx poe docs
```

## 🔁 CI/CD 工作流程总览

所有流程位于 `.github/workflows/`，以下为触发时机与用途：

- Tests（`test.yml`）

  - 触发：对 `main`、`release/*` 的 PR
  - 执行 pytest（3.11/3.12/3.13/3.14）并留下覆盖率摘要

- Code Quality（`code-quality-check.yml`）

  - 触发：PR
  - 执行 ruff 与其它 pre-commit hooks

- Docs Deploy（`deploy.yml`）

  - 触发：推送到 `main` 与 `v*` 标签
  - 构建并发布 MkDocs 网站到 GitHub Pages
  - 需在 GitHub 启用 Pages（Actions → Pages）

- Build and Release（`build_release.yml`）

  - 触发：`v*` 标签推送或手动触发
  - 构建多平台可执行文件（通过 PyInstaller）：
    - macOS（ARM64、x64）
    - Linux（x64 GNU、ARM64 GNU）
    - Windows（x64、ARM64）
  - 构建 Python 包（wheel & sdist）
  - 自动发布到 PyPI（需设置 `UV_PUBLISH_TOKEN` secret）
  - 上传所有产物至 GitHub Release
  - 注意：此为 template 示范流程，请依实际项目需求调整

- Publish Docker Image（`build_image.yml`）

  - 触发：推送到 `main` 与 `v*` 标签
  - 发布至 GHCR：`ghcr.io/<owner>/<repo>`（需 `docker/Dockerfile` 内有 `prod` target）

- Release Drafter（`release_drafter.yml`）

  - 触发：推送到 `main` 与 PR 事件
  - 基于 Conventional Commits 维护草稿发布

- PR Labeler（`auto_labeler.yml`）

  - 触发：PR 与 Push
  - 依 `.github/labeler.yml` 自动加标签

- Secret Scanning（`secret_scan.yml`）

  - 触发：Push 与 PR
  - 使用 gitleaks 扫描机密

- Semantic Pull Request（`semantic-pull-request.yml`）

  - 触发：PR 开启/更新
  - 强制 PR 标题符合 Conventional Commits

### CI/CD 设置清单

- PR 标题遵循 Conventional Commits
- （选用）发布到 PyPI：在 repository 设置中新增 `UV_PUBLISH_TOKEN` secret（Settings → Secrets and variables → Actions）
- （选用）启用 GitHub Pages 以发布文档（Settings → Pages → Source: GitHub Actions）
- （选用）发布 Docker 镜像：确认 GHCR 权限已启用（Settings → Actions → General → Workflow permissions: Read and write）

## 🧩 示例 CLI

`pyproject.toml` 内提供 `hcf_downloader` 与 `cli` 两个入口点。目前演示返回简单 `Response` 模型，可依需求替换。

```bash
uv run hcf_downloader
```

## 🤝 贡献

- 欢迎 Issue/PR
- 请遵循程序风格（ruff、类型）
- PR 标题遵循 Conventional Commits

## 📄 授权

MIT — 详见 `LICENSE`。
