n = int(input("Enter a number: "))

if n > 0 and (n % 2 == 0 or n % 5 == 0):
    print("Valid Number")
else:
    print("Invalid Number")