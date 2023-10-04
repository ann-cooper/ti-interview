import os

# closure
def outer_multiply(a):
    def inner_multiply(b):
        return a*b
    return inner_multiply

example_closure = outer_multiply(2)
demo_result = example_closure(5)  # returns 10


# decorator
def require_env_key(function):
    def wrapper(*args, **kwargs):
        key = os.getenv('MYKEY')
        if not key:
            return "error"
        else:
            return function(*args, **kwargs)
    return wrapper

# Using the decorator, if MYKEY is an environment variable, 
# running my_function will print "Hello!". Otherwise,
# it will print "error".
@require_env_key
def my_function():
    print("Hello!")