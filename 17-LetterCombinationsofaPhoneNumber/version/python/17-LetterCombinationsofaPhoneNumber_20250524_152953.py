# Last updated: 5/24/2025, 3:29:53 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        def backtracking(i, curr):
            if i == len(digits):
                if curr:
                    res.append("".join(curr))
                return
            
            for c in nums[int(digits[i])]:
                curr.append(c)
                backtracking(i + 1, curr)
                curr.pop()
        backtracking(0, [])
        return res

        

        
                
                
                