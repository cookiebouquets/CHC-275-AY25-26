""" 
OOP.py

OOP = Objected Oriented Programming

There are multiple programming paradigms:
    - Imperative: You tell the computer direct instructions to calculate things
    - Functional Programming: You're not going to touch this until your soph year of college 
    - Object Oriented Programming: You learn this in the AP and also a freshman year class
    
Motivation behind OOP:
    - in imperative programming, all state is stored under one global scope:
        - Every variable and every function has access to each other as long they persist in the same scope
        
    - Global Scope and Local Scope
        - defined in main or defined in some other function
        
    - No separation between different logical entities
        - Student directory: Every student's dictionary was exposed to each other just by calling
        directory["student name"]
        
    - This is not ideal in certain circumstances when you want logical separation between distinct 
    versions of an entity
    
    - Student
        - Grades
        - Grade Level
        - Email
        
        - Enrolling for Classes
        - Dropping Classes
        - Submitting
        - etc.
        
    Then we want some degree of separation between student A and student B. We call distinct versions
    of an entity "an instance" and we call entities "objects" 
    
    Objects are created from things called classes
    
    classes = blueprint for objects 
        - Define Member Variables (attributes)
        - Define Behaviors (methods) 
        
    every class has attributes and methods, the attributes you can specify in the constructor (a special function)
    
    and every method is exposed exclusively to that instance of the object
    
    methods = Functions, but specific to objects
    
    student has a behavior called submit(), then ONLY instances of students can use the submit function
    
    the keyword to create a class is "class"
    
    class <classname>:
"""

class student:
    """ 
    Every class requires a constructor

    constructor = a special function that you use to create an instance of an object (assign values
    to member variables)
    
    __init__(): in python double underscore = dunder 
    
    parameters would include:
        - grade level
        - grades
        - email
        - MOST IMPORTANTLY "self" object. 
        
    Think about the self object as passing in the instance of that object into the function (this will
    pass the reference of that object)
    """
    
    def __init__(self, gradelevel,grades,email,name,ssn):
        #In a constructor, typically you just do simple variable assignments 
        self.gradelevel = gradelevel #it creates a public attribute called gradelevel and assigns the
        #parameter version of gradelevel to that attribute
    
        self.email = email
        self.grades = grades
        self.name = name
        self.__ssn = ssn #social security number is local scope only
        
    def changeGrades(self): #You ALWAYS need the self parameter
        try: 
            english_grade = int(input("enter the new english grade"))
            math_grade = int(input("enter the new math grade"))
            #you NEED to derefence the member attribute through self.<attribute> to update it
            self.grades["english"] = english_grade
            self.grades["math"] = math_grade
        except:
            print("error occured")
        
        

def foo(num):
    print(num)

    
#We've defined an object with three member variables that we can create with the constructor method
def main():
    gradebook = {"english":70,"math":85}
    gradebook2 = {"english":75,"math":95}
    studentA = student(12,gradebook,"john@chc.com","john","123456789") #this creates an instance of a student
    #with the attributes 12, gradebook, john@chc.com, john. 

    """ 
    If I wanted to access those attributes, I can just dereference them using the dot notation
    """


        
    print(f"This student's name is {studentA.name}") #This student's name is john

    studentB = student(11,gradebook2,"michael@chc.com","michael","4444444")
    print(f"This student's name is {studentB.name}")

    """ 
    Object Oriented Programming is appealing for two reasons:
        1) It allows for natural code organization
            - Entities have specific attributes and behaviors that are specific to them
        2) It allows for attribute-level privacy 
        
    If we're a programmer and only studentA is exposed to us, then we cannot access the attributes and methods
    from studentB 

    what about methods? 

    Classes have two pieces
        - Attributes: Local scope variables that are tied to instances of that object
        - Methods: Specific functions thaat are tied to instances of objects 
        
    Before: 
        - every single variable and function was avaiable within the same global scope 
        - We can make function calls using any function on any variable

    After: 
        - Variables are only exposed to instances of objects
        - Function Calls are restricted to objects that are relevant to that function's behavior 
        
    """
    #To call a method, use the dot notation <variablename>.<method>()
    studentA.changeGrades() 
    print(studentA.grades)
    foo(studentA.__ssn)

""" 
Objected Oriented programming is once again appealing because naturally, when we are 
entities we want them to have behaviors that are exclusive to them:
    1) games: often have distinct entities that have behaviors and attributes that are
    specific to them  
    2) Any sort of buisness application where separability is applicable
        - Banks
        - LMS for schools
    
Object Oriented Programming historically has had a huge push since the early 90s. There
is not a single codebase out there in the professional world that does not interface
with OOP in some way. If you're writing code in these languages:
    - Python 
    - Java
    - C++
    - C# 
    - Typescript
    - Javascript
    - etc....
    
Then you are more likely than not writing OOP code. 

There is a degree of privacy involved with OOP.
    - In java/C++/most other languages, this is made explicit with the keywords
        - public and private
        
    public static void main(String[] args) {} <- main function signature in Java 
    
    what public means is that its exposed to global scope in that program. But functions
    don't necessarily have to be public. you could easily define something as private
    
    the private keyword in Java restricts the scope of that attribute/method to the local
    scope of that instance of that object
    
    To create private attributes/methods in python, we add a single _ to the prefix of that
    variable name
    
    
"""
main()

""" 
The way scoping works: 

    Def Main() <- Global Scope
        - Variables and global function signatures 
            - Instances of Students (public variables)
            - Foo
            
        - Each instance of an object has their own local scope:
            - SSN is private
            
    Def Foo() <- its own local scope
        - parameters that are passed in (that also have global scope)
        - This means that Foo(), despite passing in studentA.__ssn, does not have access
        to that attribute because its a private variable and foo doesn't have student 
        in its local scope. 


    
"""

