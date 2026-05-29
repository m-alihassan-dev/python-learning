data = {}

print("Menu: Add, Update, Delete, Search, Display, Exit")

while True:
    command = input("\nEnter Command To Perform: ").lower()

    if command == "add":
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        data[key] = value
        print("Key-Value Pair Added")

    elif command == "update":
        key = input("Enter Key To Update: ")
        if key in data:
            data[key] = input("Enter New Value: ")
            print("Value Updated")
        else:
            print("Key Not Found")

    elif command == "delete":
        key = input("Enter Key To Delete: ")
        if key in data:
            del data[key]
            print("Key Deleted")
        else:
            print("Key Not Found")

    elif command == "search":
        key = input("Enter Key To Search: ")
        if key in data:
            print(f"Found: {data[key]}")
        else:
            print("Key Not Found")

    elif command == "display":
        if data:
            print("Dictionary Contents:")
            print(data)
        else:
            print("Dictionary Is Empty")

    elif command == "exit":
        print("Exiting Program...")
        break

    else:
        print("Invalid Command")