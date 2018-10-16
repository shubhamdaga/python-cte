def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    Kevin=''
    Stuart=''
    for i in range(len(string)):
        if string[i] in 'AEIOU':
           for j in range(i,len(string)):
            a=''
            x=1
            for k in range(x):
                a=string[i,(i+k+1)]
            x=x+1
            kevin.append(a)
        else:
            for j in range(i,len(string)):
                a=''
                x=1
                for k in range(x):
                    a=string[i,(i+k+1)]
                x=x+1
                stuart.append(a)
    Kevin=list(set(Kevin))
    Stuart=list(set(Stuart))
    kevin=len(Kevin)
    stuart=len(Stuart)
    if kevin > stuart:
        print('Kevin {}'.format(kevin))
    elif Stuart>kevin:
        print('Stuart {}'.format(Stuart))
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)