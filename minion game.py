def merge_the_tools(string, k):
    # your code goes here
    n=(len(string))
    y=int(n/k)
    for i in range(0,n,y):
        a=string[i:(i+y)]
        f=''
        for j in range(len(a)):
            e=a[j]
            if a[j] in f:
                e=''
            f=f+e
        print(f)
    print(y)
    print(n)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)