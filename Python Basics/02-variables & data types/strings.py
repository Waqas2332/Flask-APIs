name = "waqas munir"
print(name.title()) # For capitalizing 1st character of each word

# changing cases

print(name.lower()) # used while storing data in database
print(name.upper())

# string concatenation

first_name = "waqas"
last_name = "munir"

print((first_name + " " + last_name).title())

# removing white spaces

name = "    Waqas    "
print(name.rstrip()) # removes white spaces from right side
print(name.lstrip()) # removes white spaces from left side
print(name.strip())  # removes white spaces from both sides

# ? In python 2, print was a keyword so parenthesis doesn't resquired but in python 3 and onwards, it acts as function thats why everything is wrapped in parenthesis