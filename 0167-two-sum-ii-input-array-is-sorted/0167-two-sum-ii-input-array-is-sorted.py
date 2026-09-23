class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1 
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return(left + 1 , right + 1)
            elif total < target:
                left += 1
            else:
                right -= 1        
            
