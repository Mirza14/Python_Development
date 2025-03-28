#Import module
import requests

x = requests.get('http://httpbin.org/get')
print(x.headers)

print(x.headers['Server'])

print(x.cookies)

print(x.status_code)

if x.status_code == 200:
    print("Success")
elif x.status_code == 402:
    print("Client Error")
else:
    print("Doesn't matter")

x = requests.get("http://httpbin.org/get", params={'id':'1'})
print(x.url)

x = requests.get("http://httpbin.org/get?id=2")
print(x.url)

x = requests.get("http://httpbin.org/get", params={'id':'3'}, headers={'Accept':'application/json'})
print(x.text)

x = requests.delete("http://httpbin.org/delete")
print(x.text)

x = requests.post("http://httpbin.org/delete", data={'a':'b'})
print(x.text)


