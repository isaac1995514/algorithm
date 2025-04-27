# Last updated: 4/27/2025, 10:52:39 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ss = min(strs, key=len)

        while ss:
            matches = map(lambda x: x.startswith(ss), strs)
            if all(matches):
                return ss
            else:
                ss = ss[:-1]
        
        return ss