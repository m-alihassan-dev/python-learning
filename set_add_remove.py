fruits = {"mango", "banana", "peach", "grapes"}

print("Fruits:", fruits)

fruit_to_add = input("Enter fruit name to add: ").lower()
fruits.add(fruit_to_add)
print("After adding:", fruits)

fruit_to_remove = input("Enter fruit name to remove: ").lower()

if fruit_to_remove in fruits:
    fruits.remove(fruit_to_remove)
    print("After removing:", fruits)
else:
    print("Fruit not found in the set!")