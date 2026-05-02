class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # create map
        adjMap = defaultdict(list)
        for u, v in adjacentPairs:
            adjMap[u].append(v)
            adjMap[v].append(u)

        # unique -> count: start, end = 1, else 2
        start = adjacentPairs[0][0]
        for key, value in adjMap.items():
            if len(value) == 1:
                start = key
                break
        
        nums = []
        seen = set() # unique
        def dfs(num):
            seen.add(num)
            for next_num in adjMap[num]:
                if next_num in seen:
                    continue
                dfs(next_num)
            nums.append(num)
        dfs(start)
        return nums
