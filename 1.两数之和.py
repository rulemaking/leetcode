#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index]+nums[index+1] == target:
                result = [index,index+1]
                return result
                
            
        
# @lc code=end

