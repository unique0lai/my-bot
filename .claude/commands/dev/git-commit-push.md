---
name: "DEV: Git Commit & Push Rules"
description: Git 提交流程与质量门禁（Conventional Commits + 禁止跳过检查）
category: Workflow
tags: [git, quality, workflow]
---

执行任何 `git commit` / `git push` 时，必须遵守以下规则。

## 必须遵守

1. 先执行代码检查与测试，再提交：
   - `uv run pre-commit run --all-files`
2. 提交信息必须遵守 Conventional Commits。
   - 示例：`feat(scope): short summary`
3. 推送前必须执行：
   - `uv run pre-commit run pytest --all-files --hook-stage pre-push`

## 明确禁止

- 禁止使用 `git commit --no-verify`
- 禁止跳过任何代码检查或测试
- 禁止在检查失败时继续提交或推送

## 例外条件

仅当用户明确授权时，才允许临时跳过检查。执行时必须：

1. 明确记录授权内容；
2. 说明跳过原因；
3. 在后续补齐所有检查。
