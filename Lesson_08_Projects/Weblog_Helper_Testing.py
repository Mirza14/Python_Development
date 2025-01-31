import ipaddress
import re

ip = ipaddress.IPv4Address("37.237.168.123")

ip_value = ip

if str(ip_value) == '37.237.168.123':
    print('Correct, IP Address')
else:
    print('Incorrect')

log_file = '/Users/mirzamansooralibaig/Desktop/Python_Development/Lesson_08_Projects/Logs.txt'

with open(log_file, 'r') as file:
    for delimeter in file:
        if re.search("159.253.133.50", delimeter):
            print('hey found it')