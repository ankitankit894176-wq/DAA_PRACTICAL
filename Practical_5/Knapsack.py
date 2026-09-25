weights=[]
values=[]

for i in range(2):
    weight=int(input("Enter weight of item "+str(i+1)+": "))
    value=int(input("Enter value of item "+str(i+1)+": "))
    weights.append(weight)
    values.append(value)

capacity=int(input("Enter capacity of knapsack: "))

dp=[[0 for j in range(capacity+1)] for i in range(3)]

for i in range(1,3):
    for j in range(1,capacity+1):
        if weights[i-1]<=j:
            dp[i][j]=max(values[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]

print("Maximum value =",dp[2][capacity])