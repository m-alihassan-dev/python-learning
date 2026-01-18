string = input("Enter String to Reverse: ")

reverse = ""
for ch in string:
    reverse = ch + reverse

print(reverse)