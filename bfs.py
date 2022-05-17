#bfs
import collections
graph={'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
         
def bfs(graph,root):
    visited = set()
    queue = collections.deque([root])
    while queue:
        vertex= queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)

bfs(graph,'0')