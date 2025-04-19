# Import module
import sys

# 1 Flag at the command line option for users
if len(sys.argv) == 1:
    print('hey')
# 2 Flags at the commad line options and 1st index should be -n and n value should be int index at 2nd
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("Meow")
else:
    print("sys.py")

print(sys.version)
print(sys.executable)
print(sys.platform)
print(sys.path)
print(sys.modules)