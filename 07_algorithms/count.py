string = input("Enter Your String: ")

digits = 0
alphabets = 0
symbols = 0

for i in string:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        alphabets += 1
    else:
        symbols += 1

print(f"Digits: {digits}\nAlphabets: {alphabets}\nSymbols: {symbols}")