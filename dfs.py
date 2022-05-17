# dfs 
graph={'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

visited = set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for nex in graph[root]:
            dfs(visited,graph,nex)

dfs(visited,graph,'0')