n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print(n, "is Positive and Even")
    else:
        print(n, "is Positive and Odd")
elif n < 0:
    print(n, "is Negative")
else:
    print(n, "is Zero")