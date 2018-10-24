def solve(s):
    list=s.split()
    list1=[]
    for i in list:
        list1.append(i[0].upper()+i[1:])
    
    string=''
    
    for i in range(len(list1)):
        string+=' '+list1[i]
    string=string[1:]
    return string

if __name__ == '__main__':
   

    s = input()

    result = solve(s)

    print(result)
