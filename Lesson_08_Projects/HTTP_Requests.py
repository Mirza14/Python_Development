#Import module
import requests

url = "https://www.aircanada.com"

def response():
    Response = requests.get(url)
    if "status" in Response.text:
        print("yay")
    else:
        print("You suck at it")

response()



