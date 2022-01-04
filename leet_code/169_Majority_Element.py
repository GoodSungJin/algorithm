# https://leetcode.com/problems/majority-element/

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    hash = {}
    majorityCount = int(len(nums) / 2)

    for num in nums:
      if hash.get(num) is None:
        hash[num] = 1
      else:
        hash[num] = hash[num] + 1

      if hash[num] > majorityCount:
        return num
