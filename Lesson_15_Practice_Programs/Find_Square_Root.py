# Problem: Write a program to find the square root of a given number

# Solution 1: Use the math module and it's methods and constants

#Import modules
import math
num = int(input("Enter a number here: "))
root = math.sqrt(num)
print("The square root of the given number is: ", root)

# Solution 2: Using exponentiation
#Exponentiation (provide power) & square root - Don't need power of a square but rather power root. This is in exponent format.

num1 = int(input("Enter your number here: "))
square = num1**(0.5) #0.5 or 1/2 denote in exponent form for square root
print("The square root of the given number is: ", square)