name = "Mirza"
age = 31
print(name.upper())
print(age.bit_length())

#Creating class
class Car:
    def __init__(self, name, year):
        self.name = name #Data Fields
        self.year = year #Data Fields
    
    ##def start(self):
        print("Engine started")

class Owner:
    def __init__(self, name, address, contact_number):
        # When we create an Owner object, we need to provide these three values
        self.name = name 
        self.address = address
        self.phone_number = contact_number
        
#Creating object (Instance)
c1 = Car("Toyota", 2020)
#c1.start()
print(c1.name)
print(c1.year)

c2 = Car("BMW", 2022)
#c2.start()
print(c2.name)
print(c2.year) 