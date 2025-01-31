# OOP

- To map with real world scenarios, we started using objects in code. This is called *Object Oriented Programming.*
- Class is a blueprint for creating objects.
- Creating class
`class Student:`
    `name = "Mirza"`
- Creating object (instance of class)
`s1 = Student()`
`print(s1.name)`

## __init__ Function

- *Constructor:* All classes have a function called `__init__()`, which is always executed when the class is being initiated.
- Creating class
`class Student:`
    `def __init__(self, fullname):`
    `self.name = fullname`
- Creating object (instance of class)
`s1 = Student("Kate")`
`print(s1.name)`
- The *self* parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
