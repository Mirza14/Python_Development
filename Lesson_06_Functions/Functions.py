# Basic function definition and call
def function1():
    print('How are you')

function1()

# Function with return values
def function2():
    return "How's things?"
store = function2()
print(store)

# Function with 1 Parameter
def function3(s):
    print((s))

function3('Test')

# Function with 2 parameters
def function4(s1, s2):
    print((s1, s2))

function4("any", "thing")
function4(s1 = '4', s2 = '9')

v = 100
print(v)

# Global Variable
def function5():
    global v
    v += 1
    print(v)

function5()
print(v)

# Function calling another function
def function6():
    print('hey from function6')

def function7():
    function6()
    print('I am from function7')

function7()

# Recursive function - a function calling itself
def function8(x):
    print(x)
    if x > 0:
        function8(x-1)

function8(5)

# Write a function that takes two arguments and returns their sum
def print_lyrics(a, b): #function definition; parameters
    return a + b

add = print_lyrics(2, 3) #function call; arguments
print(add)

# Write a function that takes three arguments and returns their average
def calculate_average(a, b, c): #function definition; parameters
    sum = a + b + c
    avg_value = sum / 3
    print(avg_value)
    return avg_value
calculate_average(5, 8, 9) #function call; arguments

# Write a function that calculates two numbers and returns the result
# Default parameter
def cal_product(a, b=2): #function definition; parameters
    print(a * b)
    return a * b
cal_product(1)


    