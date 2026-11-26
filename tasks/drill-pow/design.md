# 技术方案：drill-pow

<!-- spec-guard: review reviewer-approved dcac062c313b -->

## 现状调研

- 查了 `src/calc.py`：现有 `add`、`sub`、`mul` 三个函数，都直接返回运算结果，不做类型校验。
- 查了 `tests/test_calc.py`：用 `unittest` 逐个函数写测试；测试命令为 `python3 -B -m unittest discover -s tests -v`。
- 没查：CI 配置与 `.github/` 下的文件，本模块不改它们。

## 影响面

会改到的已有文件：

- `src/calc.py`：新增 `power(a, n)`，不改已有函数。
- `tests/test_calc.py`：新增 `power` 的测试类，不改已有测试。

## 实现方案

`power(a, n)` 先检查 `n`：不是 `int` 或小于 0 时抛 `ValueError`；否则用循环连乘 `n` 次得到结果，`n == 0` 时返回 `1`。不用内置 `**`，以便与"整数次幂"的定义一一对应、测试能覆盖每条分支。

## 接口和数据改动

新增公开函数 `power(a, n) -> a ** n`（`n` 为非负整数）。没有数据或配置改动。

## 风险与回滚

风险只在 `src/calc.py` 被误改导致已有函数出错，由回归测试文档里「受影响的老功能」一节的用例兜住。回滚就是 revert 实现 PR。

## 方案取舍

- 直接 `return a ** n`：更短，但负指数会返回小数而不是报错，需要另加判断；连乘写法让规则和代码对应更直观。
- 放进新文件 `src/power.py`：能避开已有文件，但本次演练要验证「碰了老逻辑必审」与「受影响的老功能」用例，所以放进 `src/calc.py`。

## 外部审查意见

<!-- spec-guard: design-review round=1 blocking=0 sha256=7b21bf3acdde vendor=openai same-vendor=false criteria=design-v1 report=97ae2e26accaeb481d0a3725797e1072b5ed15874e674820f31040261541384e -->
