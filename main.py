# Justin Goff
# CIS261
# WK8 Lab 2 - Fibonacci

def fib_seq(x):
    n = 0
    n1,n2 = 0,1
    fib_string = ""
    print(f"The Fibonacci sequance for {x} ")
    if x == 1:
        print(n1)
    else:
        while n < x:
            fib_string += str(n1) + ", "
            sum = n1 + n2
            n1 = n2
            n2 = sum
            n += 1
        fib_string += "..."
        print(fib_string)

fib_seq(16)