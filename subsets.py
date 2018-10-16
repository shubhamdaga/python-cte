iterations=int(input())
for x in range(iterations):
	no_of_a=int(input())
	a=set(map(int,input().split()))
	no_of_b=int(input())
	b=set(map(int,input().split()))
	print(b.issubset(a))