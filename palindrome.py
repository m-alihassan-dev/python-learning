n = int(input("Enter a Number: "))

num = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if rev == num:
    print(num, "is Palindrome")
else:
    print(num, "is not Palindrome")