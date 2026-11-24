class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def bfs(graph, visited, source):
            q = deque()
            q.append(source)
            visited.add(source)
            while q:
                node = q.popleft()
                for i in range(len(isConnected)):
                    if isConnected[node][i] == 1 and i not in visited:
                        q.append(i)
                        visited.add(i)
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                bfs(isConnected, visited, i)
                count += 1
        return count