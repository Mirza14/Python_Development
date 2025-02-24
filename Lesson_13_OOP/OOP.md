# OOP

- To map with real world scenarios, we started using objects in code. This is called *Object Oriented Programming.*
- Everything we create in Python is object. We can manipulate the data that object contains using in-built methods.
- Class is a blueprint for creating objects. Class defines how an object should look like.
- Creating class
`class Student:`
    `name = "Mirza"`
- Creating object (instance of class)
`s1 = Student()`
`print(s1.name)`

## __init__ Function

- *Constructor:* All classes have a function called `__init__()`, which is always executed when the class is being initiated.
- init is a special method in Python, allows us to set up some data fields or data for the class. It only runs once when object is instantiated.
- By defining an init, we can add data fields to an object, which allows us to initialize object.
- Creating class
`class Student:`
    `def __init__(self, fullname):`
    `self.name = fullname`
- Creating object (instance of class)
`s1 = Student("Kate")`
`print(s1.name)`
- The *self* parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
