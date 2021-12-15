# https://leetcode.com/problems/two-sum/

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_map = {}

    for i in range(len(nums)):
      value = target - nums[i]

      if hash_map.get(value) is not None and hash_map[value] != i:
        return [hash_map[target - nums[i]], i]

      hash_map[nums[i]] = i
