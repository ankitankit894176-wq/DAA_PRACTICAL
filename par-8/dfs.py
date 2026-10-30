
def dfs(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(graph,n,visited)
graph={0:[1,2],1:[0,3],2:[0,4],3:[1,4],4:[2,3]}
print("DFS Traversal:")
dfs(graph,0,set())
