n=int(input("Enter order of matrix : "))
sum=int(n*(n*n+1)/2)
mat=[]
row=[]
mat=[[0 for i in range(n)]for j in range(n)]
for e in range(1,n*n+1):
    if e==1:
        i,j=n//2,n-1
    else :
        i-=1
        j+=1
        if i==-1 and j !=n:
            i=n-1
        elif i !=-1 and j==n:
            j=0
        elif i==-1 and j==n:
            i=0
            j=n-2
        if mat[i][j] !=0:
            i+=1
            j-=2
    mat[i][j] = e
for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()