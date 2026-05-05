#oop2.py

""" 
Yesterday I showed you:
    -the class keyword
    -Described the point of OOD
    
The idea is we can naturally separate different entities from each other with their
own respective attributes and functions

Each individual concept (person, animal, etc.) has their own
    - attributes
    - behaviors
    
and their state (the computer science definition of state) do not overlap.

You can define special behaviors that are exclusive to instances of objects 
which are just explicit examples of those

students 
    - name
    - email
    - grades
    - ssn (private variable)
    
    - change grades

We can create student objects that correspond to different individual students

The benefit of this is clear:
    1) We have a natural degree of separation of information that pertains to only
    one example (everything was stored in one dictionary in lab 6)
    2) Behaviors that are exclusive to one instance of an object can only be called
    for that instance (less room for error)
    
Beginning "advanced" python with things like dunder functions 
    - __init__() <= creating a new instance of that object
        - int() is an __init__ function, __str__ is an dunder function, etc. 
    
    ^ this is the start of understanding how python works as a programming languages
    
The thing that distinguishes python from other languages
    - The syntax (non important feature) 
    - Data Model (Everything in python is an object dervied by the use of 
    dunder functions)
    
integers are objects, strings are objects, lists are objects, dictionaries are objects,
etc. 

Every single object in python is quite literally the SAME object, as in every time
you create a new class, you get acces to the same dunder functions, but its
implementation defined on what those dunder functions do 

lists and dictionaries are really the same "kind" of object fundamentally they
both collect information under a single variable name

but lists and dictionaries have different implementations for their respective dunder
functions 

lists and dictionaries have different __getitem__ functions 

list.__getitem__(index)
list[index]

dict.__getitem__(key)
dict[key]

Understanding how to use the python data model to your advantange (abusing dunder
functions) is the difference between someone who knows python and someone who is an 
expert at it 

^ We're going to return to this in a second but we really should talk about inheritance
first 

inheritance is really a fundamental concept in OOP, dunder function magic is specific 
to python

Inheritance = How you can pass shared behaviors from one class to another

Person 
    - Name
    - Social Security Number
    - Address 
    - Phone Number
    
A person is the top level abstraction that contains attributes that is true
for every single US Citizen. We can define a second level abstraction that is role
specific. We can define classes that behave like a person, but contain new behaviors
that are exclusive to the roles that we define
"""

class Person:
    def __init__(self,name,ssn,address,num):
        self.name = name
        self.__ssn = ssn #dunder before a variable name gives it private scope
        self.address = address
        self.phone = num
        
    def greetings(self):
        print(f"Hello, I am {self.name}, my address is {self.address}, and my phone number is {self.phone}")
        

personA = Person("John","123456789","Lasalle rd","1111111")
personA.greetings() 

""" 
So a person has these basic attributes, but we can define
a role specific class that INHERITS those same features
"""

class Student(Person): 
    #student has the same attributes as person, plus
    #whatever additional things we define
    def __init__(self, name, ssn, address, num,school):
        super().__init__(name, ssn, address, num)
        #if we call super().__init__(), it'll call
        #the person level constructor first and then allow
        #us to define student specific attributes 
        self.school = school
        
    def greetings(self):
       print(f"Hello, I am {self.name}, my address is {self.address}, and my phone number is {self.phone}")
       print(f"I also attend {self.school}")
    
studentA = Student("michael","22222222222",
                   "lasallerd","33333","chc")

studentA.greetings()

""" 
the super() prefix allows you to
    1) still use the original behaviors from the parent class
    2) also overload (change) the behavior to the specific child class you're working on

A lot of strange things can happen as a result of inheritance 

A
B inherits from A 
    - overloads behavior a
C inherits from A 
    - overloads behavior a
D inherits from B and C 

what happens when you call D.a? <= questions like this are so common on the AP, common in your OOP class (spring semester
freshman year in college), pretty common in job interviews too 

If you're trying to get an internship 
    - C++ has a lot of OOP nuances and they'll kill you over this 
    
The point is that inheritance allows you to modify behaviors of things that already exist 

^ Everything technically inherits from a parent object Object
"""

""" 
1 + 1  = 2
"1" + "1" = "11"
"""

class SpecialNumber():
    def __init__(self,value):
        self.value = value
        
    def __add__(self, other): #overloading the addition sign
        return 2*self.value + 2*other.value
    
num1 = SpecialNumber(4)
num2 = SpecialNumber(2)

print(num1 + num2) # 2*4 + 2*2 = 8 + 4 = 12

