# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description

#BEST SOLUTION!
# 1-st Solution compl: O(n), memory: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
        return k