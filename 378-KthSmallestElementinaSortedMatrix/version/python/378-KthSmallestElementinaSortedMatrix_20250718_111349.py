# Last updated: 7/18/2025, 11:13:49 AM
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]

        while l < r:
            mid = (l + r) // 2
            s = 0
            c = n - 1

            for row in matrix:
                while c >= 0 and row[c] > mid:
                    c -= 1
                s += c + 1

            if s < k:
                l = mid + 1
            else:
                r = mid

        return l

