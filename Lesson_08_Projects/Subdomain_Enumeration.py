#Import Modules
import requests
import sys

#Simple GET request
web = requests.get("https://tryhackme.com/")
print(web.status_code)

#File Handling
list = open("/Users/mirzamansooralibaig/Downloads/wordlist2-1626415171030.txt").read()
sub_doms = list.splitlines()

#Looping through a list
for sub in sub_doms:
    sub_domains = f"http://{sub}.{"tryhackme.com"}"

    #Exception Handling
    try:
        requests.get(sub_domains)

    except:
        requests.ConnectionError
        pass

    else:
        print("Valid Domain: ", sub_domains)



