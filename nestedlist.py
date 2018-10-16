list1=[]
marks=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        marks.append(score)
marks1=marks
marks1.sort()
print(marks1)
marks1=set(marks1)
print(marks1)
marks1=list(marks1)
print(marks1)
marks1.sort()
print(marks1)
second_lowest=marks1[1]
name=[]
for i in range(len(list1)):
    if second_lowest==list1[i][1]:
        name.append(list1[i][0])
name.sort()
for i in name:
    print(i)
