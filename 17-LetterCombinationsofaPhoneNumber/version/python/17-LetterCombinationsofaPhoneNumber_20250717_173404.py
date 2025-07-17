# Last updated: 7/17/2025, 5:34:04 PM
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

        

        
                
                
                