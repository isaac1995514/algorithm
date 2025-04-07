# Last updated: 4/7/2025, 5:44:45 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break;
                print(i, j)
                if j == len(needle) - 1:
                    return i
        
        return -1
