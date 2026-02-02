numbers = [1, 2, 3, 4, 5]

squares_list = [n * n for n in numbers]        # List Comprehension
squares_set = {n * n for n in numbers}         # Set Comprehension
squares_dict = {n: n * n for n in numbers}     # Dictionary Comprehension

print(squares_list)
print(squares_set)
print(squares_dict)