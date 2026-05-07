with open("test.py","r") as f:
    program = f.readlines() #The text you need this to be a single 
    
program = compile(program,"test","exec")
exec(program)