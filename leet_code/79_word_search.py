# https://leetcode.com/problems/word-search/
# 시간 초과 나옴 다시 풀어봐야함 아직은 못하겠음

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      def find_word(word, x, y):
        direction = [
          [0, -1],  # top
          [1, 0],  # right
          [0, 1],  # bottom
          [-1, 0]  # left
        ]

        if len(word) == 0:
          return True

        if (x < 0 or x >= len(board[0])) or \
            (y < 0 or y >= len(board)) or \
            board[y][x] == '.' or \
            word[0] != board[y][x]:
          return False
        board[y][x] = '.'

        for moveX, moveY in direction:
          if find_word(word[1:], x + moveX, y + moveY):
            return True

        board[y][x] = word[0]

      for y in range(len(board)):
        for x in range(len(board[0])):
          if find_word(word, x, y):
            return True
      return False
