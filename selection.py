# selection sort

A=[6,2,7,1,4]

for i in range(len(A)):
    mini= i
    for j in range(i+1,len(A)):
        if(A[mini]>A[j]):
            mini=j 
    A[i],A[mini] = A[mini],A[i]

print(A), 