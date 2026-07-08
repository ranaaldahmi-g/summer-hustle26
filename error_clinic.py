
#I predict that it wont work because it was dividing by zero and it will give me an error message

x = 10
y = 0
result = x * y
print("Result:", result)

# I predict it wont work because of the + 1 on line 13

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

# I predict it wont work because there are no indents

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))

# I predict it wont work because of the missing colon at the end of the if statement

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    return False
print(is_even(4))
print(is_even(7))

# I predict it wont work because of the missing colon at the end of the for loop

for i in range(5):
    print(i)

# I predict it wont work because of the indents

def greet(name):
    return "Hello, " + name
print(greet("Alice"))

# I predict it wont work because there are no indents

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

# I predict this also wont work because there are no indents

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# I predict it will not work because of the indents

name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")


# I predict it will not work because of the indents

def divide_numbers(x, y):
    result = x / y
    return result
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))