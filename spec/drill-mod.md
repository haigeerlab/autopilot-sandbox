# 需求：drill-mod

<!-- spec-guard: review approved d50a1c119cf2 -->

<!-- spec-guard: flow v2 tier=small -->

## 目标

给 `src/calc.py` 加一个取余函数 `mod(a, b)`，返回 `a % b`，并补上测试。这是 autopilot hub-auto-merge 检查点 5 的演练（回归用例 R14、R15），用来在沙盒里端到端跑通自动路：会话调一次 `hub run`，由 GitHub 自动合并，合并后由本机 watch 收尾。

## 给谁用

只给检查点 5 的演练用，没有真实用户。

## 使用场景

演练时，实现 PR 改 `src/calc.py` 与 `tests/test_calc.py`，autopilot 按本文档的回归用例验证后打开自动合并。

## 业务规则和异常情形

- `mod(7, 3) == 1`。
- `b` 为 0 时抛出 `ValueError`。
- 参数是数字，不做类型校验（与 `add`、`sub`、`mul` 一致）。

## 不做什么

- 不改动已有的 `add`、`sub`、`mul`、`power`，不改 CI 或其他配置。

## 成功标准

- S1：`mod(7, 3) == 1`。
- S2：`b` 为 0 时抛出 `ValueError`。
- S3：已有函数不受影响，原有测试仍全部通过。

## 待定问题

无。

## 做法

在 `src/calc.py` 末尾加 `mod(a, b)`：`b == 0` 时抛 `ValueError("除数 b 不能为 0")`，否则返回 `a % b`。在 `tests/test_calc.py` 加 `ModTest`，覆盖 S1、S2。

## 回归用例

### R1: 取余结果与异常
- 步骤：运行 `mod` 的单元测试
- 预期：`mod(7, 3) == 1`；`b` 为 0 时抛 `ValueError`
- 执行方式：command
- 命令：`python3 -B -m unittest discover -s tests -p test_calc.py -k ModTest -v`
- 证据：运行输出

### R2: 原有测试仍通过
- 步骤：运行全部单元测试
- 预期：全部通过
- 执行方式：command
- 命令：`python3 -B -m unittest discover -s tests -v`
- 证据：运行输出

| 成功标准 | 用例 |
|---|---|
| S1 | R1 |
| S2 | R1 |
| S3 | R2 |

## 变更记录

- 2026-11-27：用户在对话里确认需求复述，原话「对」。
