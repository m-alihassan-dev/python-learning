t = int(input("Enter Temperature: "))

if t < 0:
    print("Freezing Cold")
elif t < 10:
    print("Very Cold")
elif t < 20:
    print("Cold")
elif t < 30:
    print("Pleasant")
elif t < 40:
    print("Hot")
else:
    print("Very Hot")