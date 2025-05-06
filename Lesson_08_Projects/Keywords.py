#Import Modules
import re

#Logic
def extract_ips_with_keyword(filename, keyword="login"):
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                ips = ip_pattern.findall(line)
                if ips:
                    print(line.strip())
                    print("IPs:", re.findall(ip_pattern, line))

# Example usage:
extract_ips_with_keyword('/Users/mirzamansooralibaig/Desktop/Python_Development/Lesson_08_Projects/Logs.txt')
