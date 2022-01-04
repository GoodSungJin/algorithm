# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) <= 0:
      return 0
    
    curr = nums[0]
    ctn = 1
    
    for i in range(1, len(nums)):
      if curr != nums[i]:
        nums[ctn] = nums[i]
        curr = nums[i]
        ctn += 1
        
    return ctn
