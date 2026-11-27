# Plan：drill-mod

## 任务

- Task 1：在 `src/calc.py` 加 `mod(a, b)`，在 `tests/test_calc.py` 加 `ModTest`。验证：回归用例 R1、R2 的命令都通过。
- Task 3：在 `tests/test_calc.py` 加 `MainRedDrillTest`：只在 GitHub Actions 的 push 事件里故意失败，其他环境通过（hub-auto-merge 检查点 5 R15 ② 演练：让主干 push CI 变红，演练后撤回）。验证：本机与 PR 上回归用例 R1、R2 通过。

## 检查点

- Checkpoint 1（gate）：实现 PR 由 autopilot 做合并前验证（R1、R2 自动执行），通过后打开 GitHub 自动合并，合并后由 watch 收尾。
