# Problem: Print 5 times

print("What's the story? \n" * 5)

fruit = str(input("Write down your favourite fruit: "))
print("Your favourite fruit is ", fruit)

for x in fruit:
    print((fruit + "\n") * 50)