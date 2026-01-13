num = int(input("Enter a number: "))

if num > 0 and (num % 2 == 0 or num % 5 == 0):
    print("Valid Number")
else:
    print("Invalid Number")