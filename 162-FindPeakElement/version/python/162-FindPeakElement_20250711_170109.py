# Last updated: 7/11/2025, 5:01:09 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(m)
            if nums[m] > (nums[m-1] if m > 0 else float('-inf')) and nums[m] > (nums[m+1] if m < len(nums) - 1 else float('-inf')):
                return m
            elif nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m - 1
        
        return l

                