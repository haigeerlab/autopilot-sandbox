"""Tiny module the autopilot drills change."""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def power(a, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("指数 n 必须是非负整数")
    result = 1
    for _ in range(n):
        result *= a
    return result


def mod(a, b):
    if b == 0:
        raise ValueError("除数 b 不能为 0")
    return a % b
