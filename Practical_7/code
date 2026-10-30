def coin_change(coins,amount):
	dp=[float('inf')]*(amount+1)
	dp[0]=0
	coin_used=[-1]*(amount+1)
	for i in range(1,amount+1):
		for coin in coins:
			if i>=coin and dp[i-coin]+1<dp[i]:
				dp[i]=dp[i-coin]+1
				coin_used[i]=coin
	if dp[amount]==float('inf'):
		print("Change not possible")
		return
	print("Minimum coins needed:",dp[amount])
	curr=amount
	ans=[]
	while curr>0:
		ans.append(coin_used[curr])
		curr-=coin_used[curr]
	print("Coins used:",ans)
coins=list(map(int,input("Enter coin denominations: ").split()))
amount=int(input("Enter amount: "))
coin_change(coins,amount)
