#Import Modules
import requests
url = 'https://assets.tryhackme.com/img/THMlogo.png'

#HTTP GET Request
r = requests.get(url, allow_redirects=True)
open('THMlogo.png', 'wb').write(r.content)
