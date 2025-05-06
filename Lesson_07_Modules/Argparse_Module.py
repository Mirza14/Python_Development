#Import Modules - Argument Parser
import argparse

#Initializing the parser
#Variable called parser and set it equal to return value of argparse.ArgumentParser. A constructor for a class called arugment parser that comes with Python itself.
parser = argparse.ArgumentParser(description="Meow like a cat")

#Positional Arguments. Method in the parser object. Configure this Argument Parseer to know about specific command line arguments.
parser.add_argument("-n", default=1, type=int, help="Number of times to meow")

#Parse the command line arguments. parse_args() is going to look at sys.argv
#args is the object returned by parse_args()
args = parser.parse_args()
for _ in range(args.n):
    print("Meow")