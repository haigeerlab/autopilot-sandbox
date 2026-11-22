# Implementation Plan: drill-div

<!-- spec-guard: review codex-approved 4cb3cd727ad0 -->

## Overview

一步完成：新增 `src/divide.py` 和 `tests/test_divide.py`。

## Architecture Decisions

- 除数为 0 时显式抛 `ValueError`，而不是让 Python 抛 `ZeroDivisionError`，便于调用方统一处理参数错误。

## 影响面

只新增 `src/divide.py`、`tests/test_divide.py`。

## Task List

### Phase 1：实现

- Task 1：`div` 与测试（验收 1、2、3、4）
  - 验证：`python3 -B -m unittest discover -s tests -v` 全绿

### Checkpoint 1（gate）：模块最终验收

- 由 Codex 对照本 Spec 审"开工前提交 → HEAD"的补丁，并核对 autopilot 在 HEAD 上写的检查证据（非作者跑过、全部退出 0）；两者都绑定 HEAD 才记验收。

## 外部审查意见

<!-- spec-guard: codex-review round=1 blocking=0 sha256=272ec260a78c -->
