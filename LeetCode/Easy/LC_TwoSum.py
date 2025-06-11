# https://leetcode.com/problems/two-sum/

#BEST SOLUTION!
# 1-st Solution compl: O(n**2), memory: O(1)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j] 
                
