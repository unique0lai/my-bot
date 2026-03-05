# AGENTS

本文件用于说明本项目中人类与 AI Agent 的协作基线。

## 目标

- 保持代码可读、可测试、可维护。
- 任何变更都应通过 lint、类型检查和测试。
- 提交历史保持结构化与可追踪。

## 技术栈与布局

- Python 3.13+
- `src` 布局（包路径：`src/my_bot`）
- 测试目录：`tests`
- 包管理/运行：`uv`

## 必要质量门禁

- `ruff check .`
- `basedpyright`
- `pytest`
- `pre-commit` hooks 全部通过

## Git 提交流程

1. 开发完成后运行：
   - `uv run ruff check .`
   - `uv run basedpyright`
   - `uv run pytest`
2. 执行提交，提交信息必须符合 Conventional Commits。
3. 推送前确保 `pre-push` 阶段测试通过。
4. 执行 `git commit` / `git push` 时，优先使用 `uv run git ...`（如 `uv run git commit ...`、`uv run git push`），避免 hooks 因找不到 `pre-commit` 失败。

## Conventional Commits 约束

允许的提交前缀示例：

- `feat:` 新功能
- `fix:` 修复
- `docs:` 文档
- `refactor:` 重构
- `test:` 测试
- `chore:` 杂项

示例：

- `feat: add CLI entrypoint`
- `fix: prevent None access in parser`
- `test: add unit tests for main module`

## 变更原则

- 小步提交，避免一次提交包含不相关改动。
- 非必要不引入新依赖。
- 优先修复根因，不做表面补丁。
- 新增功能默认补充测试或解释不补测试的原因。

## 注释与文档字符串规范

- 开发过程中应添加合适的注释，重点说明复杂逻辑、边界条件与关键设计取舍。
- 所有函数和类必须编写 docstring。
- docstring 风格统一使用 Google 风格。
