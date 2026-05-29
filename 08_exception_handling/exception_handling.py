try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division By Zero Is Not Allowed")

except ValueError:
    print("Error: Please Enter Numbers Only")

except Exception as e:
    print("Unexpected Error Occurred:", e)