# Week 5 Object Oriented Programming
Everything in Python is an object and has a type. Object is a data abstraction that captures internal representation through data attribute, interface for interacting with object through methods hiding implementation. A tuple, list, dictionary are built-in object types but one can also create her own data object type. Internal representation of data should be private and one should use defined interface instead of manipulating the internal representation directly.

### Advantages of OOP
+ Bundle data into packages with procedures so one can use well-defined interface
+ Divide and conquer development which allow a programmer to implement and test behavior of each class
+ Easier to reuse code as in python, each class has a separate environment
+ Advantages of inheritances to redefine or extend a behavior of superclass

Data attribute means other objects that make up the class. procedural attributes can be understood as functions that only work with this class. Many operators such as +, -, ==, print, len() can override to work with your class by re-defining

Class is the type while instance is one particular object. Class is defined generically and class defines data and methods common across all instances while data values vary between instances because though two instances can be inherited from same class they care different objects.

It is convention to have getter and setter to access data attribute to prevent bugs and to better maintain code.

### Hierarchies
Child class(also called subclass) inherits all data and behaviors of parent class and also add more info, add more behavior and override behaviors. ```__init__()```is a keyword to inherits all attributes of parent class. For an instance of a class, it looks for a invoked method name in current class
