# 回归测试：drill-pow

## 用例清单

### R1: 幂函数的结果与异常
- 步骤：运行 `power` 的单元测试
- 预期：`power(2, 10) == 1024`、`power(5, 0) == 1`；指数为负数时抛 `ValueError`
- 执行方式：command
- 命令：`python3 -B -m unittest discover -s tests -p test_calc.py -k PowerTest -v`
- 证据：运行输出

### R2: 用户亲手试一次
- 步骤：在沙盒检出里运行 `python3 -B -c "import sys; sys.path.insert(0, 'src'); import calc; print(calc.power(3, 4))"`
- 预期：输出 `81`
- 执行方式：manual
- 证据：用户原话

## 成功标准对照

| 成功标准 | 用例 |
|---|---|
| S1 | R1、R2 |
| S2 | R1 |
| S3 | R3 |

## 受影响的老功能

### R3: 已有的加减乘不受影响
- 步骤：运行全部测试
- 预期：原有测试全部通过
- 执行方式：command
- 命令：`python3 -B -m unittest discover -s tests -v`
- 证据：运行输出
