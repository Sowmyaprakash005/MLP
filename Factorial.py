# CODING 1 - FACTORIAL WITHOUT BUILT-IN FUNCTIONS

n = 5
a = 1

for i in range(1, n + 1):
    a = a * i

print(a)


# CODING 2 - FACTORIAL USING RECURSION

n = int(input("Enter a number: "))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print("The factorial of given number is:", fact(n))
