# Lockboxes Project

## Overview

The Lockboxes project is designed to solve the problem of determining whether a series of locked boxes can all be opened. Each box is numbered sequentially from `0` to `n - 1`, and may contain keys to other boxes. The goal is to write a method that determines if all the boxes can be opened.

## Function Prototype

```python
def canUnlockAll(boxes)
```

### Parameters

- `boxes`: A list of lists, where each inner list contains keys (positive integers) that correspond to the indices of other boxes.

### Assumptions

- A key with the same number as a box opens that box.
- All keys are positive integers.
- There may be keys that do not correspond to any box.
- The first box (`boxes[0]`) is initially unlocked.

### Returns

- `True` if all boxes can be opened.
- `False` if not all boxes can be opened.

### Problem Description

You are presented with `n` locked boxes, each numbered from `0` to `n - 1`. Each box may contain several keys, and each key corresponds to a specific box number. Your task is to determine if you can open all the boxes, starting from the first box, which is already unlocked.
