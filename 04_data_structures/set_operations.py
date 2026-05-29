set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"First set: {set_a}")
print(f"Second set: {set_b}")

print("\nAvailable operations:")
print("union, intersection, difference, symmetric_difference")

choice = input("Enter operation you want to perform: ").lower()

if choice == "union":
    print(f"Union: {set_a | set_b}")
elif choice == "intersection":
    print(f"Intersection: {set_a & set_b}")
elif choice == "difference":
    print(f"Difference (A - B): {set_a - set_b}")
elif choice == "symmetric_difference":
    print(f"Symmetric Difference: {set_a ^ set_b}")
else:
    print("Invalid operation!")