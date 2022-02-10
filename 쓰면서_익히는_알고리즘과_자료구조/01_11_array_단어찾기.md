# 부분 집합
고유한 정수의 집합으로 배열이 주어지면 가능한 모든 부분집합을 반환하자. 중복된 부분집합은 허용하지 않는다.

입력으로 [1, 2, 3]이 주어지면, 결과로 [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]을 반환하면 된다.

<br>

## 학습 전
### 문제 접근
```text
제한사항
- 왔던 길을 다시 되돌아 갈 수 없다.
- 인접한 요소로만 갈 수 있다.
- 2차원 배열로 들어온다.

아이디어 (재귀)
- 아직 생각을 정의하지 못하겠음... 그냥 이렇게 하면 될 것 같아서 했음...
- 긴 배열은 시간초과남
```

### 문제 풀이
```python
def exist(board: list[list[str]], word: str) -> bool:
  direction = [
    [0, -1],  # top
    [1, 0],  # right
    [0, 1],  # bottom
    [-1, 0]  # left
  ]

  def find_word(subword, x, y):
    if len(subword) == 0:
      return True

    if (x < 0 or x >= len(board[0])) or \
        (y < 0 or y >= len(board)) or \
        board[y][x] == '.' or \
        subword[0] != board[y][x]:
      return False

    board[y][x] = '.'

    for moveX, moveY in direction:
      if find_word(subword[1:], x + moveX, y + moveY):
        return True

    board[y][x] = subword[0]

  for y in range(len(board)):
    for x in range(len(board[0])):
      if find_word(word, x, y):
        return True
  return False
```

