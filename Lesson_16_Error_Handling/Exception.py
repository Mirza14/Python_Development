print(1)

try:
  f = open("/Desktop/Python_Development/Lesson_12_File_Handling/roc.txt")
except FileNotFoundError:
  print("The file does not exist")
except Exception as e:
  print(e)
finally:
  print("I am going to print anyway")

n = 100
if n == 0:
  raise Exception("n can't be 0!")
if type(n) is not int:
  raise Exception("n must be an int!")

n = 0
assert(n != 0)
print(1/n)
