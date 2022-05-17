#N-Queens

n= int(input("Enter number "))
board=[]

def getboard():
    for i in range(n):
        nList=[]
        for j in range(n):
            nList.append(0)
        board.append(nList)

def printBoard():
    for i in range(n):
        for j in range(n):
            print(board[i][j],end="")
        print("")

def isSafe(row,col):
    for i in range(n):
        if board[row][i] == 1:
            return False
    for j in range(n):
        if board[j][col] == 1:
            return False
    row=i-1
    col=j-1 
    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i=i-1
        j=j-1
        
    row=i-1
    col=j+1 
    while(i>=0 and j<n):
        if board[i][j]==1:
            return False
        i=i-1
        j=j+1
    row=i+1
    col=j-1 
    while(i<n and j>=0):
        if board[i][j]==1:
            return False
        i=i+1
        j=j-1
    row=i+1
    col=j+1 
    while(i<n and j<n):
        if board[i][j]==1:
            return False
        i=i+1
        j=j+1
    return True
    
def put(n,count):
    if count==n:
        return True
    for i in range(n):
        for j in range(n):
            if isSafe(i,j):
                board[i][j]=1 
                count +=1 
                if put(n,count)==True:
                    return True
                board[i][j]=0
                count -=1 
    return False
    
getboard()
put(n,0)
printBoard()