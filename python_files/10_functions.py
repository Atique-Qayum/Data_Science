# a function is a block of code which only runs when it is called.
# you can pass data, known as parameters, into a function.
# a function can return data as a result.
# in python a function is defined using the def keyword:


# lets define a function

def greet_user():
    print("hello, user!")

greet_user()


def aoa(name):
    print(f"This is {name}!")

aoa("Atique")

def aoa(name = "User"):
    print(f"This is {name}!")

aoa()

# return values

def square(number):
    return number * number

result = square(3)
print(result)

# recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))


# lambda function

x = lambda a : a + 10               # input value + 10
y = lambda a, b : a + b             # input value and add them
z = lambda a, b=5 : a + b           

print(x(5))
print(y(5, 6))
print(z(5))