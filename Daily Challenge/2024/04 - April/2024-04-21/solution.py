class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False] * n
        # we try for a bfs impl
        queue = []
        cur = source
        while True:
            if cur == destination:
                return True # got to destination
            else:
                visited[cur] = True
                for edge in edges:
                    if edge[0] == cur:
                        if not visited[edge[1]]:
                            queue.append(edge[1])
                            visited[edge[1]] = True
                    elif edge[1] == cur:
                        if not visited[edge[0]]:
                            queue.append(edge[0])
                            visited[edge[0]] = True
            if len(queue) == 0:
                break
            cur = queue.pop(0)
        return False
