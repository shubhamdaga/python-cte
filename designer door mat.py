list=(input().split())
l=[]
for c in list:
	l.append(int(c))
N=l[0]
M=l[1]
b=((M-1)//2)-1
f=1
for a in range(int((N-1)/2)):
	d="-"*(b)
	e=".|."*(f)
	print(d+e+d)
	b=b-3
	f=f+2
print(("-"*(((M-1)//2)-3))+"WELCOME"+("-"*(((M-1)//2)-3)))

b=3
f=(M-6)//3
for a in range(int((N-1)/2)):
	d="-"*(b)
	e=".|."*(f)
	print(d+e+d)
	b=b+3
	f=f-2

