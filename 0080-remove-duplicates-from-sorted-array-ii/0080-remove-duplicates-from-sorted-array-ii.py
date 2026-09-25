class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        
        for right in range(len(nums)):
           
            if left < 2:
                nums[left] = nums[right]
                left += 1
            elif nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left +=1
        return left         
