def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter Number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"Factorial of {n} is {factorial(n)}")