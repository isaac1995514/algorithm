# Last updated: 7/17/2025, 6:00:57 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        res = []
        for s in spells:
            left, right = 0, m - 1
            first = m
            while left <= right:
                mid = (left + right) // 2

                # If equal or greater, record and move left
                if s * potions[mid] >= success:
                    first = mid
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(m - first)
        
        return res
            
            
                    
            
