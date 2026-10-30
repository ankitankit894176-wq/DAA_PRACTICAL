
from collections import deque
def bfs(graph,start):
    visited={start}
    queue=deque([start])
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
graph={0:[1,2],1:[0,3],2:[0,4],3:[1,4],4:[2,3]}
print("BFS Traversal:")
bfs(graph,0)
