# https://leetcode.com/problems/pascals-triangle/

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    pascal = [[1]]

    for i in range(1, numRows):
      row = [1]

      for j in range(1, i + 1):
        if j < i:
          prevNum = pascal[i - 1][j - 1]
          nextNum = pascal[i - 1][j]

          row.append(prevNum + nextNum)
        else:
          row.append(1)
      pascal.append(row)

    return pascal
