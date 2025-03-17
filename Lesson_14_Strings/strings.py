string1 = 'hey' # single quotes
string2 = "hello"  # double quotes
string3 = '''how are you?''' # triple quotes
string4 = """What is new with you?
Tell me something interesting. 
I'm all ears."""

print(string1)
print(string2)
print(string3)
print(string4)

string5 = "I'm alright!" # using double quotes inside single quotes
string6 = "I\"m good" # using escape character

print(string5)
print(string6)

string7 = "I'm fantastic!\n""I will come around to see you soon." # using escape character for a new line
print(string7)

string8 = 'a' * 10 # string multiplication
print(string8)

print(len(string8)) # length of a string

print("how" in string3) # check if a string is in another string to evaluate to True or False
print("new" in string3) # check if a string is in another string to evaluate to True or False

print(string3.startswith("how")) # check if a string starts with another string to evaluate to True or False
print(string2.index("l")) # find the index of a character in a string
print(string1.upper()) # convert a string to uppercase
print(string2.lower()) # convert a string to lowercase

space_string = "    I have spaces before and after me.    "
print(space_string.strip()) # remove spaces before and after a string
print(space_string.replace("I", "You").strip()) # replace a character in a string with another character
print(space_string.replace(".", "!").strip()) # replace a character in a string with another character

print(space_string.split()) # split a string into a list of words

string9 = "I am a String"
print(string9)
print(string9.encode())
print(string9.encode("utf-8"))

print(string9.rjust(10))
print(string9.rjust(10, "X"))

print("I am " + "a string")
print("string9 is " + str(len(string9)) + "characters")

# F-string allows you to format selected parts of a string. To specify a string as an f-string, simply put an f in front of the string literal.
# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

print("string9 is {} characters long!".format(len(string9))) # Format String

print("{} {}".format(len(string9), 5.0, 0x12)) # Format String

length = len(string9)
print(f"string9 is {length} characters long") # Format String

print(f"string9 is {length:.2f} characters long".format(len(string9))) # Float
print(f"string9 is {length:x} characters long") # Hex

