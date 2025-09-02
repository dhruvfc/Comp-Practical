def Armstrong(n):
    if n>=0:
        n1=n
        a=0
        l=len(str(n))
        while n>0:
            r=n%10
            r**=1
            a+=r
            n//=10
        if a==n1:
            return 'Armstrong'
        else:
            return 'Not Armstrong'
    else:
        return 'Not Armstrong'
n = int(input('Enter a Number: '))
print(Armstrong(n))
