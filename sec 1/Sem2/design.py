#design.py

"""
Before I release the next lab, we need to cover some design considerations. 

This semester: 
    - Functions
        - Pass by Value vs Pass by Reference:
            - passing an integer or a list as an argument for a function changes the behavior 
        - Local vs Global Scope:
            - Each codeblock has its own "scope" as in they cant see outside of its own scope
        - We have deep levels of code reusability. 
            - the whole point of the async assignments was to show that we can write a single procedure
            and reuse it for multiple kinds of inputs. 
            
    - most of software engineering is writing functions. In that sense, functions allow for collaboration 
    in an easier way, multiple people can work on multiple functions at the same time. You can expose your
    functions to other programmers that they can call within their programs. 
        - These are called APIs, we are exposing functionality to other programmers for them to use
        in their own programs
        
    - Up until this point, the way we wrote programs was largely unstructured. We just dumped in linjes
    of code into a blank file and expected the program to execute from line 1. <- this gets messy quick
    
    - There are design considerations we have to make when it comes to writing larger programs. 
    
    - When we write functions, they don't have to be executed immediately. So we can define a function
    on line 1, and that function could never get called at any point in a program. We should not mix
    function definitions with code we expect to execute. 0
"""

    
#foo()

#^ this kind of design really sucks, we have functions definitions interspersed with lines of code
#that is being executed. 

""" 
Why does this suck? 

    1. We have lines of code is not being executed in the same space as lines being executed, i.e.
        we can't tell what is being ran and what isn't being ran just by glancing at it.
    2. We're exposing ourselves to making a lot of mistakes. Python cares a lot about indentation,
        we are exposing ourselves to making critical errors with our functions because we might make a white
        space error
    3. Functions aren't exposed to you until the interpreter gets to that line of code. 
        - So if I need a function but don't declare it until way further into the program, then I can't
        use that function until the interpreter gets to that function definition. 
        
        
So there has to be a natural way to layout our program so that we can circumvent all of these issues at once. 

Just like how you are writing a paper for English, there is a "correct" way to lay out a program. 
    - We should have functions placed at the very top of our program.
    - We should have the actual lines of code we expect to execute at the bottom. 

So that leads me to discussing the main function. We have never used def main() before in a piece of code. 

What the main function is: its the function that gets executed when the program is run. 
    - python is a command line program
    - when we hit the run button on vscode, its really executing this script in our terminal
        - python <filename> 
        
    python is going to look for a main function definition and execute that line of code. 
"""
x = 5

def foo():
    print("hello")
    
y = 6
def bar():
    print("bar")
    
import functions

    
def main():
    x = 5 
    y = 6 #more clear as to which scope x and y belongs to. 
    foo()
    functions.add5(x)

if __name__ == "__main__": #two underscores on both sides of name and main
    main()
    
""" 
Why do this at all? Adding all of this structure to the program makes this program much more complicated
than it has to be. 

I told you that scope matters: 
    - We want all of our global variables to be obviously in the same scope 
    - We can straight up import other python files into our program, and we get unexpected behavior if we 
    don't explicitly write this if name procedure. 
    
"""



