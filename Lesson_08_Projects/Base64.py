#Import Module
import base64

#File Handling
b64_s = open("/Users/mirzamansooralibaig/Downloads/b64_1550406728131.txt","r")
data = b64_s.read()

#Function definition
def decode():
    #Decode to get bytes object
    for bytes in b64_s:
        sample_bytes = base64.b64decode(bytes)
    #Conver bytes object to a String
    print(sample_bytes.decode("utf-8"))

decode()