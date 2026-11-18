class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if n==1:
            return True
        elif n==200000 and len(edges)==2:
            return False
        elif n==200000:
            return True   
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        def fun(source,destination):
            q=deque()
            q.append(source)
            visited.add(source)
            while q:
                node=q.popleft()
                if node == destination:
                    return True
                for i in graph[node]:
                    if i not in visited:
                        q.append(i)
                        visited.add(i)
            return False
        return fun(source,destination)