# Snippet 1
# x = 10
# y = 0
# result = x / y
# print("Result:", result)
x = 10
y = 0
if y != 0:
    result = x / y
    print("Result:", result)
else:
    print("Cannot divide by zero")
# PREDICT: ZeroDivisionError

# Snippet 2
# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     print(numbers[i + 1])
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
# PREDICT: IndexError

# Snippet 3
# def calculate_area(radius):
#     area = 3.14 * radius ** 2
#     return area
# radius = 5
# print(calculate_area(radius))
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))
# PREDICT: SyntaxError

# Snippet 4
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(4))
# print(is_even(7))
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
# PREDICT: SyntaxError

# Snippet 5
# for i in range(5):
#     print(i)
for i in range(5):
    print(i)
# PREDICT: SyntaxError

# Snippet 6
# def greet(name):
#     return "Hello, " name
# print(greet("Alice"))
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
# PREDICT: SyntaxError

# Snippet 7
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for number in numbers:
#     total += number
# print("Sum of numbers:", total)
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("Sum of numbers:", total)
# PREDICT: IndentationError

# Snippet 8
# def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n + 1)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# PREDICT: Logic error

# Snippet 9
# name = input("Enter your name: ")
# if name == "Alice" or "Bob":
#     print("Hello, " + name)
# else:
#     print("Hello, stranger!")

name = input("Enter your name: ")

if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")

# PREDICT: Logic error


# Snippet 10
# def divide_numbers(x, y):
#     result = x / y
#     return result
# num1 = 10
# num2 = 0
# print(divide_numbers(num1, num2))

def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))

# PREDICT: ZeroDivisionError