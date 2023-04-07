def multiply(times):
    return lambda f: lambda  *args, **kwargs: times * f(*args, **kwargs)

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))
