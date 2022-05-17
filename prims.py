#Prims

INF = 9999999
N=5
G=[[0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]]
num_edge =0
selected = [0,0,0,0,0]
selected[0] = True

while(num_edge<N-1):
    mini = INF
    a=0
    b=0
    for m in range(N):
        if selected[m]:
            for n in range(N):
                if ((not selected[n]) and G[m][n]):
                    if mini>G[m][n]:
                        mini=G[m][n]
                        a=m 
                        b=n 
    print(str(a)+'-'+str(b)+':'+str(G[a][b]))
    selected[b]=True
    num_edge +=1