def palindrome(n):
    n1=n
    r=0
    while n>0:
        a=n%10
        r*=10
        r+=a
        n//=10
    if r==n1:
        return 'It is Palindrome Number'
    else:
        return 'It is not Palindrome Number'
n=int(input("Enter a Number: "))
print(palindrome(n))
