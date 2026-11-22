# Spec: drill-div

<!-- spec-guard: review codex-approved a06dc4fb9fb2 -->

## 目标

新增 `src/divide.py`，提供除法函数 `div(a, b)`，并补上测试。这是 autopilot 第二批演练 2 的重演：接管配置（#5）先于本 Spec 单独提交，用来跑通 spec-guard 模块的"接管到合并"链路。

## 范围

- 新增 `src/divide.py`，内含 `div(a, b)`；
- 新增 `tests/test_divide.py`。

不做：改动 `src/calc.py`、已有测试、CI 或配置文件。

## 假设

- 参数是数字，不做类型校验（与 `src/calc.py` 一致）。

## 接口约定

- `div(a, b) -> a / b`；
- `b == 0` 时抛出 `ValueError`，消息为 `除数不能为 0`。

## 项目结构

只新增 `src/divide.py`、`tests/test_divide.py`。

## 并行边界

- 独占：`src/divide.py`、`tests/test_divide.py`
- 公共：无

## 命令

测试：`python3 -B -m unittest discover -s tests -v`

## 测试策略

单元测试覆盖整除、非整除、负数各一例，以及除数为 0 时抛 `ValueError`。

## 边界

只新增上面两个文件；不加依赖。

## 验收标准

1. `div(6, 3) == 2`、`div(7, 2) == 3.5`、`div(-6, 3) == -2`；
2. `div(1, 0)` 抛出 `ValueError`，消息为 `除数不能为 0`；
3. 已有测试仍全部通过；
4. 以本模块开工前的提交（本 Spec 首次提交的父提交）为基准，实现 PR 的代码改动只涉及 `src/divide.py`、`tests/test_divide.py`；spec-guard 自己的产物（本模块的 Spec、Plan、todo）不计。

## 未决问题

无。

## 外部审查意见

<!-- spec-guard: codex-review round=1 blocking=0 sha256=6b81e01cb6ea -->
