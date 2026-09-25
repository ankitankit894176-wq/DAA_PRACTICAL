n=int(input("Enter number of matrices: "))
p=[]
for i in range(n+1):
    p.append(int(input("Enter dimension "+str(i+1)+": ")))

dp=[[0 for j in range(n)] for i in range(n)]

for length in range(2,n+1):
    for i in range(n-length+1):
        j=i+length-1
        dp[i][j]=999999999
        for k in range(i,j):
            cost=dp[i][k]+dp[k+1][j]+p[i]*p[k+1]*p[j+1]
            if cost<dp[i][j]:
                dp[i][j]=cost

print("Minimum number of multiplications =",dp[0][n-1])