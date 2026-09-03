class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            current_product = nums[i]

            if current_product < 0:
                max_product , min_product = min_product, max_product

            max_product = max(current_product ,max_product * current_product)
            min_product = min( current_product, min_product * current_product) 

            answer = max(answer, max_product)   
        return answer

