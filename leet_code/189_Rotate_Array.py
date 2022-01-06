# https://leetcode.com/problems/rotate-array/

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    count = 0

    for start in range(k):
      if count >= len(nums):
        break
      prev_index = start
      prev_num = nums[start]

      while True:
        next_index = (prev_index + k) % len(nums)
        temp_num = nums[next_index]
        nums[next_index] = prev_num
        prev_num = temp_num

        prev_index = next_index
        count += 1

        if prev_index == start:
          break
