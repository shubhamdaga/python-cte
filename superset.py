a=set(map(int,input().split()))
iterations=int(input())
answer=True
for i in range(iterations):
	
	b=set(map(int,input().split()))
	shit=False
	if b.issubset(a):
		shit=True
	elif b==a:
		shit=True
	else:
		shit=False
	if shit==False:
		answer=False
print(answer)

