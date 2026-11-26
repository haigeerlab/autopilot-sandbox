# 需求：drill-pow

<!-- spec-guard: review approved fdaae296fa3d -->

<!-- spec-guard: flow v2 tier=normal -->

## 目标

给 `src/calc.py` 加一个整数幂函数 `power(a, n)`，返回 `a` 的 `n` 次方，并补上测试。这是 autopilot S110 的 S6 演练，用来在沙盒里跑通 spec-guard 新流程模块的全链路：需求由用户确认、技术方案由第二审查者审、按回归测试文档做合并前验证、机器人合并、意见转跟进 issue。

## 给谁用

只给 autopilot 的 S6 演练用，没有真实用户。

## 使用场景

演练时，实现 PR 改 `src/calc.py` 与 `tests/test_calc.py`，autopilot 按本模块的回归测试文档验证后决定是否合并。

## 业务规则和异常情形

- `power(a, 0)` 返回 `1`。
- `n` 为负数时抛出 `ValueError`。
- 参数 `a` 是数字，不做类型校验（与 `add`、`sub`、`mul` 一致）。

## 不做什么

- 不支持小数指数。
- 不考虑性能。
- 不改动已有的 `add`、`sub`、`mul`，不改 CI 或其他配置。

## 成功标准

- S1：`power(2, 10) == 1024`。
- S2：指数为负数时抛出 `ValueError`。
- S3：已有的 `add`、`sub`、`mul` 不受影响，原有测试仍全部通过。

## 待定问题

无。

## 变更记录

- 2026-11-26：用户在对话里确认需求与档位，原话「对，drill-pow 接管到合并」。
