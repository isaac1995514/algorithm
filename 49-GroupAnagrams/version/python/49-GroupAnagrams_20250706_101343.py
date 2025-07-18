# Last updated: 7/6/2025, 10:13:43 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(s)
        
        return list(hash_map.values())

