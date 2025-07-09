# Last updated: 7/8/2025, 8:24:04 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = nums[:]
        res = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] *= right[i + 1]
        left = 1

        for i in range(n-1):
            res[i] = left * right[i + 1]
            left *= nums[i]
        res[-1] = left

        return res

        
        
