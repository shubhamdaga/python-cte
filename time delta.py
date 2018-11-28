import math
import os
import random
import re
import sys
from datetime import datatime

def month(l):
	if l=="Jan":
		return 1
	elif l="Feb":
		return 2
	elif l="Mar":
		return 3
	elif l="Apr":
		return 4
	elif l="May":
		return 5
	elif l="Jun":
		return 6
	elif l="Jul":
		return 7
	elif l="Aug":
		return 8
	elif l="Sep":
		return 9
	elif l="Oct":
		return 10
	elif l="Nov":
		return 11
	else:
		return 12
def time_delta(t1,t2):
	answer=0
	T1=t1.split()
	T2=t2.split()
	T1[3]=month(T1[3])
	T2[3]=month(T2[3])
	if int(T1[3])>=int(T2[3]):
		answer+=(int(T1[3])-int(T2[3]))*31557600
		if T1[]

	else:
		answer+=(int(T2[3])-int(T1[3]))*31557600
	print(T1,T2)

t = int(input())
for t_itr in range(t):
	t1 = input()
	t2 = input()
	delta = time_delta(t1, t2)
	print(delta)