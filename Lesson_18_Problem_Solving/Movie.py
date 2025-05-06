# Weekdays
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Age
age = int(input("How old are you? "))
weekday = str(input("What day is today? "))
price = 12

if age >=18 and not week[3]:
    print(f"Your ticket price is {price}")
elif age <18 and not week[3]:
    print (f"Your ticker price is {price-4}")
elif age >=18 and week[3]:
    print(f"Your ticket price is {price-2}")
elif age <18 and week[3]:
    print (f"Your ticker price is {price-2}")
else:
    print("You are having a bad day, sorry!")