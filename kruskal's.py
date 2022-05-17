#kruskal's algo


def find(graph,node):
    if graph[node]<0:
        return node
    else:
        return find(graph,graph[node])
        
def union(graph,a,b,answer):
    ta=a 
    tb=b 
    a = find(graph,a)
    b = find(graph,b)
    if a==b:
        pass
    else:
        answer.append([ta,tb])
        if graph[a]<graph[b]:
            graph[a] +=graph[b]
            graph[b]=a 
        else:
            graph[b] +=graph[a]
            graph[a]=b

inp = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
    ]
n=4    
answer=[]

inp = sorted(inp, key=lambda inp:inp[2])
graph = [-1] * (n+1)
for u,v,d in inp:
    union(graph,u,v,answer)
print(answer)