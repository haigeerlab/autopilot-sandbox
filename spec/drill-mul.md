# Spec: drill-mul

<!-- spec-guard: review codex-approved 5ec970a16851 -->

## 目标

给 `src/calc.py` 加一个乘法函数 `mul(a, b)`，返回 `a * b`，并补上测试。这是 autopilot 第二批的演练 2，用来跑通 spec-guard 模块的"接管到合并"链路。

## 范围

- 在 `src/calc.py` 新增 `mul(a, b)`；
- 在 `tests/test_calc.py` 新增对应测试。

不做：改动已有的 `add`、`sub`；改动 CI、配置或其他文件。

## 假设

- 参数是数字，不做类型校验（与 `add`、`sub` 一致）。

## 接口约定

`mul(a, b) -> a * b`

## 项目结构

只动 `src/calc.py`、`tests/test_calc.py`。

## 并行边界

- 独占：`src/calc.py`、`tests/test_calc.py`
- 公共：无

## 命令

测试：`python3 -B -m unittest discover -s tests -v`

## 测试策略

单元测试覆盖正数、零、负数各一例。

## 边界

只改上面两个文件；不加依赖。

## 验收标准

1. `mul(3, 4) == 12`、`mul(5, 0) == 0`、`mul(-2, 3) == -6`；
2. 已有测试仍全部通过；
3. 以模块开工前的提交（本 Spec 与 Plan 获批后合入的 `main`）为基准，实现 PR 的代码改动只涉及 `src/calc.py`、`tests/test_calc.py`；spec-guard 自己的产物（`tasks/drill-mul/todo.md` 勾选）不计。

## 未决问题

无。

## 外部审查意见

<!-- spec-guard: codex-review round=1 blocking=0 sha256=93aacd21e21d -->
<!-- spec-guard: codex-review round=2 blocking=1 sha256=5290d3245e13 -->
<!-- spec-guard: codex-review round=3 blocking=0 sha256=ca24f077e782 -->
