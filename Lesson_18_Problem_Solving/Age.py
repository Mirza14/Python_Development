# Input Function
age = int(input("Can you enter your age to confirm the seniority? "))

# Conditionals
if age < 13:
    print("You can go to the Child's group")
elif age <= 13 and age <=19:
    print("You can go to the Teen's group")
elif age <= 20 and age <=50:
    print("You can go to the Adult's group")
elif age >= 60:
    print("You can go to Senior Citizen's group")
else:
    print("You don't qualify our seniority, sorry")