"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]"""






N=int(input())
answer=[]
for i in range(N):
	choice=input()
	if 'insert' in choice:
		d=choice.split()
		position=d[1]
		value=d[2]
		answer.insert(int(position),int(value))
	if 'print' in choice:
		print(answer)
	if 'remove' in choice:
		d=choice.split()
		number=int(d[1])
		answer.remove(number)
	if 'append'in choice:
		d=choice.split()
		number=int(d[1])
		answer.append(number)
	if 'sort' in choice:
		answer.sort()
	if 'pop' in choice:
		answer.pop()
	if 'reverse' in choice:
		answer.reverse()



















