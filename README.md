# my-bot

一个使用 `src` 布局的 Python 示例项目，内置以下工程化能力：

- 代码风格与静态检查：`ruff`
- 类型检查：`basedpyright`
- 单元测试：`pytest`
- Git 提交前/推送前自动检查：`pre-commit`
- 提交信息规范校验：`Conventional Commits`

## 目录结构

```text
.
├── src/
│   └── my_bot/
│       ├── __init__.py
│       ├── __main__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── .pre-commit-config.yaml
└── pyproject.toml
```

## 环境准备

```bash
uv sync --dev
```

项目默认使用 PyPI 镜像源：`https://mirrors.cloud.tencent.com/pypi/simple/`（见 `pyproject.toml` 的 `tool.uv.index-url`）。

## 常用命令

```bash
# 运行程序
uv run python -m my_bot

# 代码检查
uv run ruff check .
uv run basedpyright

# 运行测试
uv run pytest

# 手动执行 pre-commit
uv run pre-commit run --all-files
uv run pre-commit run pytest --all-files --hook-stage pre-push
```

## 安装 Git Hooks

```bash
uv run pre-commit install --hook-type pre-commit --hook-type pre-push --hook-type commit-msg
```

## 提交信息规范（Conventional Commits）

提交信息必须符合 Conventional Commits，例如：

- `feat: add health check endpoint`
- `fix: handle empty input`
- `docs: update README`
- `chore: bump dev dependencies`

不符合规范的提交信息会在 `commit-msg` 阶段被拒绝。
