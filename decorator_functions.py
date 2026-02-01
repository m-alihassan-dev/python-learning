def decorator(function):

    def wrapper(*args, **kwargs):
        print("Calling Function:", function.__name__)
        print("Positional Arguments:", args)
        print("Keyword Arguments:", kwargs)

        result = function(*args, **kwargs)

        print("Return Value:", result)
        print("-" * 40)

        return result

    return wrapper

@decorator
def calculate_total(price, quantity, discount=0):
    return price * quantity - discount

# Testing the Decorator
total = calculate_total(100, 2, discount=10)
print(total)