# OOP

- To map with real world scenarios, we started using objects in code. This is called *Object Oriented Programming.*
- Everything we create in Python is object. We can manipulate the data that object contains using in-built methods.
- Why Class? To create own custom data types and give them names. A Class is like a mold that you can define and give a name and when you use that mold/blueprint you get types of data that are designed exactly as you want.
- In short, Classes allow you to invent your own data types in Python and give them a name.
- Class is a blueprint for creating objects (Pieces of data objects). Class defines how an object should look like. Anytime you create a Class you are creating an object.
- You create objects from classes. An object is when you use that mold/buleprint to build a specific house
- Classes have attributes or properties that allow you to specify values inside of them.
- Class is definition of a new data type and object is instances of classes. Class can store attributes inside of it using a (.dot) notation and you can access those same attributes.
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
