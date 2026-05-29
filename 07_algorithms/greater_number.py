a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print("Both numbers are the same")