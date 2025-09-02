def fib(n):
    if n <= 0:
        print("Please Enter a Positive Number.")
        return
    elif n == 1:
        print("Fibonacci Series: ", 0)
        return
    elif n == 2:
        print("Fibonacci Series: ", 0, 1)
        return
    a, b = 0, 1
    print("Fibonacci Series: ", a, b, end=" ")
    for i in range(n-2):
        a, b = b, a+b
        print(b, end=" ")
n = int(input("Enter Number of Elements in Series: "))
fib(n)
