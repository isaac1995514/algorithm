# Last updated: 7/6/2025, 10:19:08 AM
class UnionFind:
    def __init__(self, nums):
        self.parent = {}
        self.size = {}
        self.max_size = 0
        for num in nums:
            self.parent[num] = num
            self.size[num] = 1
            self.max_size = 1
    
    def find(self, i):
        if self.parent[i] == i:
            return self.parent[i]
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        if i not in self.parent or j not in self.parent:
            return False
        
        root_i, root_j = self.find(i), self.find(j)

        if root_i == root_j:
            return False

        if self.size[root_i] < self.size[root_j]:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
            self.max_size = max(self.max_size, self.size[root_j])
        else:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.max_size = max(self.max_size, self.size[root_i])
        
        return True
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)

        for num in nums:
            uf.union(num, num + 1)
            uf.union(num, num - 1)
        return uf.max_size
        

        