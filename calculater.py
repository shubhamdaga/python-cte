import firstmodule
firstno=input().strip()
secondno=input().strip()
import math
if firstno=='e':
	firstno=math.e
elif secondno=='e':
	secondno=math.e
elif firstno=='pi':
	firstno=math.pi
elif secondno=='pi':
	secondno=math.pi
else:
	firstno=int(firstno)
	secondno=int(secondno)

cal=input()

if cal=='add':
	print(firstmodule.add(float(firstno),float(secondno)))
if cal=='sub':
	print(firstmodule.sub(float(firstno),float(secondno)))
if cal=='mul':
	print(firstmodule.mul(float(firstno),float(secondno)))
if cal=='div':
	print(firstmodule.div(float(firstno),float(secondno)))