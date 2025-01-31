#Documentation: https://docs.python.org/3/library/argparse.html & https://docs.python.org/3/library/ipaddress.html

#Import Modules
import argparse
import ipaddress

#Function Definition
def ip_cidr_Filter(ip_cidr, logfile):
    try:
        #Parse user's input as an IP network for single IPs or CIDR ranges
        network = ipaddress.ip_network(ip_cidr, strict=False)
    except:
        print(f"Invalid IP or CIDR notation: {ip_cidr}")
        return
    
    #File Handling
    with open(logfile, 'r') as file:
        #Looping through a file
        for delimeter in file:
            #Extract the IP address from the start of each line in a String
            log_ip = delimeter.split()[0]
            try:
                #Check if the log IP is in the specified network
                if ipaddress.ip_address(log_ip) in network:
                    print(delimeter.strip())
            except:
                #Skip lines with invalid IP formats
                continue

def main():
    #Initializing the Parser
    parser = argparse.ArgumentParser()
    
    #Positional Arguments
    parser.add_argument("--ip", required=True, help="Filter the given IP Address or CIDR Range")
    parser.add_argument("Logfile", help="Please provide the path to the logfile")
    
    #Parse the Arguments
    args = parser.parse_args()
    
    #Function Calling
    ip_cidr_Filter(args.ip, args.Logfile)

if __name__ == "__main__":
    main()


               
