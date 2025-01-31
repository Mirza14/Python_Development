names = ['Alice', 'Bob', 'Liam', 'Dan']
gender = ['female', 'male', 'male', 'male']

def print_elements(list):
    for i in list:
        print(i, end=" ")

print_elements(names)
print_elements(gender)

# Write a function that calculates the factorial of a number
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(7)

# Write a function that does the conersion of a Euro amount to a Rupee amount
def euro_to_rupee(euro):
    inr = euro * 90
    print(euro, "EURO =", inr, "INR")

euro_to_rupee(25)