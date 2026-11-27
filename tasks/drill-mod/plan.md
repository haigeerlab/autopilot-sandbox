# Plan：drill-mod

## 任务

- Task 1：在 `src/calc.py` 加 `mod(a, b)`，在 `tests/test_calc.py` 加 `ModTest`。验证：回归用例 R1、R2 的命令都通过。
- Task 2：在 `tests/test_calc.py` 的 `ModTest` 补负数被除数的测试（`mod(-7, 3) == 2`，与 Python `%` 一致）。验证：回归用例 R1、R2 的命令都通过。

## 检查点

- Checkpoint 1（gate）：实现 PR 由 autopilot 做合并前验证（R1、R2 自动执行），通过后打开 GitHub 自动合并，合并后由 watch 收尾。
