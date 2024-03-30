

def greet(name):
    print(f"Hello {name.title()}!" )
    
    
greet("Waqas") # positional argument

greet(name="Waqas") # keyword argument

# passing optional arguments

def formatName(firstName,lastName,middleName=""):
    if middleName:
        return f"{firstName.title()} {middleName.title()} {lastName.title()}"
    else:
        return f"{firstName.title()} {lastName.title()}"
    
print(formatName(firstName="Waqas",lastName="Munir"))
print(formatName("Muhammad","Munir","Waqas"))