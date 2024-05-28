# 🏰 0x05. N Queens Challenge 🏰

Welcome to the **N Queens** project! This classic problem in computer science and mathematics involves placing N non-attacking queens on an N×N chessboard using the backtracking algorithm. Dive in to solve this intriguing puzzle and sharpen your algorithmic skills!

## 🧩 The N Queens Puzzle

The challenge is to place N queens on an N×N chessboard such that no two queens can attack each other. This means no two queens can share the same row, column, or diagonal.

## 🚀 Challenge Instructions

### Usage

```sh
$ nqueens N
```

- **N** must be an integer greater than or equal to 4.

### Requirements

- If the program is called with the wrong number of arguments, it should print:
  ```sh
  Usage: nqueens N
  ```
  and exit with status 1.
- If **N** is not an integer, print:
  ```sh
  N must be a number
  ```
  and exit with status 1.
- If **N** is less than 4, print:
  ```sh
  N must be at least 4
  ```
  and exit with status 1.

### Output

- The program should print every possible solution to the N queens problem.
- Each solution should be printed on a new line.
- Each solution should follow this format:
  ```sh
  [[row, col], [row, col], ..., [row, col]]
  ```
- Solutions do not need to be printed in any specific order.

## 🛠️ Requirements

- **Python version**: 3.x
- **Imports**: Only the `sys` module is allowed.

## 📚 Key Concepts

To succeed in this challenge, familiarize yourself with:
- **Backtracking algorithms**: Essential for generating all possible solutions.
- **Chessboard representation**: Understanding how to map the N×N board to a list of coordinates.
- **Problem constraints**: Ensuring your program handles invalid inputs gracefully.

## 🌟 Example

Here's a simple example for N=4:

```sh
$ nqueens 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## 🔗 Resources

- [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)
- [N Queens on GeeksforGeeks](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/)
- [Python sys Module](https://docs.python.org/3/library/sys.html)
