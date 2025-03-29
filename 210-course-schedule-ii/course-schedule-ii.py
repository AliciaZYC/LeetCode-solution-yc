class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         # Step 1: Build the graph (adjacency list)
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # To take `course`, must first take `prereq`
        
        # Step 2: Initialize visited list
        # 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        res = []

        # Step 3: DFS function with cycle detection
        def dfs_hasCycle(node: int) -> bool:
            if visited[node] == 1:
                return True  # Found a cycle
            if visited[node] == 2:
                return False  # Already visited, no cycle

            visited[node] = 1  # Mark as visiting
            for neighbor in graph[node]:
                if dfs_hasCycle(neighbor):  # If cycle is found in deeper call
                    return True
            visited[node] = 2  # Mark as visited
            res.append(node)  # Append to result post-DFS
            return False

        # Step 4: Run DFS for each course
        for i in range(numCourses):
            if visited[i] == 0:
                if dfs_hasCycle(i):  # Cycle detected
                    return []

        # Step 5: Reverse the result to get correct topological order
        return res[::-1]
