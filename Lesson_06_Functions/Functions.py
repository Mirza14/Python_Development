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


    