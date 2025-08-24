
# Decorator function
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@decorator_function
def hello():
    print("Hello, world!")
# Using the decorator

# hello = decorator_function(hello)
hello()
# Output:   


@decorator_function
def add(a, b):
    print(f"The sum is: {a + b}")
# Using the decorated function
add(5, 10)
# Output: The sum is: 15
