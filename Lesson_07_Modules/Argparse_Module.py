#Import Modules
import argparse

#Initializing the parser
parser = argparse.ArgumentParser()

#Positional Arguments
parser.add_argument("hey")

# Parse the arguments
args = parser.parse_args()
print(args.hey)