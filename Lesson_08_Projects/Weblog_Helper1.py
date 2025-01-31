#Documentation: https://docs.python.org/3/library/argparse.html

# Import Modules
import argparse

#Function Definition
def ip_Filter(ip_address, logfile):
    #File Handling
    with open(logfile, "r") as file: 
        #Looping through a file
        for delimeter in file:
            #Condition Evaluation
            if ip_address in delimeter:
                print(delimeter.strip())

def main():
#Initializing the Parser
  parser = argparse.ArgumentParser()

#Positional Arguments
  parser.add_argument("--ip", required=True, help="Filter the given IP Address")
  parser.add_argument("Logfile", help="Please provide the path to the logfile")

#Parse the Arguments
  args = parser.parse_args()

#Function Calling
  ip_Filter(args.ip, args.Logfile)

if __name__ == "__main__":
    main()
