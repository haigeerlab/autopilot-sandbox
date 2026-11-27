# Capability Map: autopilot 沙盒演练

> autopilot 第二批演练用。每个模块对应一次"接管到合并"的完整链路演练。

## 目标

在沙盒仓库里，用 spec-guard 管理的小模块，演练 autopilot 从审查、检查、最终验收到机器人自动合并的完整链路。

## 模块

| Module id | Responsibility | Depends on |
|---|---|---|
| drill-mul | 给 `src/calc.py` 加乘法函数 `mul(a, b)` 及其测试（演练 2：spec-guard 模块自动合并） | — |
| drill-div | 新增 `src/divide.py` 的除法函数 `div(a, b)` 及其测试（演练 2 重演：配置与 Spec 分两次提交） | — |
| drill-pow | 给 `src/calc.py` 加整数幂函数 `power(a, n)` 及其测试（S110 S6：新流程全链路演练） | — |
| drill-mod | 给 `src/calc.py` 加取余函数 `mod(a, b)` 及其测试（hub-auto-merge 检查点 5：自动路端到端演练） | — |

Build order: drill-mul → drill-div → drill-pow → drill-mod

---

## 审阅记录

- [x] 模块边界确认
- [x] 依赖方向单向无环
- [x] module id 已定稿
- [x] 构建顺序符合依赖拓扑

审阅人：用户（2026-11-22，原话"沙盒的 drill-mul 模块合并设为自动"，同意按预览配置沙盒）
日期：2026-11-22
