class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        uf = UnionFind(n)
        group_cnt = n
        for timestamp, friend_a, friend_b in logs:
            if uf.union(friend_a, friend_b):
                group_cnt -= 1
            if group_cnt == 1:
                return timestamp
        return -1
class UnionFind:
    def __init__(self,size):
        self.group = [group_id for group_id in range(size)]
        self.rank = [0] * size
    def find(self,person):
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]
    def union(self,x,y):
        groupx = self.find(x)
        groupy = self.find(y)
        is_merge = False
        if groupx == groupy:
            return is_merge
        is_merge = True
        if self.rank[groupx] > self.rank[groupy]:
            self.group[groupy] = groupx
        elif self.rank[groupx] < self.rank[groupy]:
            self.group[groupx] = groupy
        else:
            self.group[groupx] = groupy
            self.rank[groupy] += 1
        return is_merge