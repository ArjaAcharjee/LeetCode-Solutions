class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        
        count = 0
        n = len(nums)

        for right in range(n -1 , 1, -1):
            
            left = 0
            end = right - 1
           
            while left < end:
                
                if nums[left] + nums[end] > nums[right]:
                    count += end - left
                    end -= 1

                else:
                    left += 1
        return count             
        