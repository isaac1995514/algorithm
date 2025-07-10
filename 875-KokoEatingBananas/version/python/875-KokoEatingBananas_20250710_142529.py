# Last updated: 7/10/2025, 2:25:29 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hourNeed(speed):
            return sum(map(lambda x: ceil(x / speed), piles))
        
        left, right = 1, max(piles)
        res = 0
        while left <= right:
            mid = (left + right) // 2

            if hourNeed(mid) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res
