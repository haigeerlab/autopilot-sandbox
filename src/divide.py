"""Division for the autopilot drill (module drill-div)."""


def div(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b
