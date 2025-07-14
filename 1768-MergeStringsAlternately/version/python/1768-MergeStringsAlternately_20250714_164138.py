# Last updated: 7/14/2025, 4:41:38 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        res = ""

        for i in range(0, min_len):
            res += word1[i]
            res += word2[i]
        
        if len(word1) < len(word2):
            res += word2[min_len:]
        else:
            res += word1[min_len:]

        return res; 