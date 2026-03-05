# AI Assistant Instructions

## Git 基础流程

1. 完成修改后先同步执行代码检查与测试。
2. 仅在检查通过后执行 `git add` 与 `git commit`。
3. 本地验证通过后执行 `git push`。

## 提交信息规范

- 所有提交信息必须遵守 Conventional Commits。
- 推荐格式：`type(scope): subject`。
- 示例：`feat(ci): add commit-msg hook for conventional commits`。

## 代码检查约束

- 禁止跳过代码检查与测试。
- 禁止使用 `--no-verify` 绕过 Git hooks。
- 仅在明确获得用户允许后，才可临时跳过检查，并需在说明中记录原因。

## 本项目默认检查

- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest`
- `uv run pre-commit run --all-files`
- `uv run pre-commit run pytest --all-files --hook-stage pre-push`
