from itertools import permutations
n=int(input("Enter number of cities: "))
cost=[]
print("Enter cost matrix:")
for i in range(n):
	cost.append(list(map(int,input().split())))
min_cost=float('inf')
best_path=None
for path in permutations(range(1,n)):
	current=0
	total=0
	valid=True
	for city in path:
		if cost[current][city]>=999:
			valid=False
			break
		total+=cost[current][city]
		current=city
	if valid and cost[current][0]<999:
		total+=cost[current][0]
		if total<min_cost:
			min_cost=total
			best_path=(0,)+path+(0,)
if best_path:
	print("Minimum Cost:",min_cost)
	print("Best Path:"," -> ".join(str(city+1) for city in best_path))
else:
	print("No valid tour found")
