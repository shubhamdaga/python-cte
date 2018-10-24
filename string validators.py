if __name__ == '__main__':
    s = input()
    a=False
    b=a
    x=a
    y=a
    z=a
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            x=True
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            y=True
        if i in '1234567890':
            z=True
        if i in 'abcdefghijklmnopqrstuvwxyz':
            a=True
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            b=True
    print(x)
    print(y)
    print(z)
    print(b)
    print(a)
            