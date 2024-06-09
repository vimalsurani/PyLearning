# String - Bunch of character

# Single  ''
name = 'Vimal'
print(name)

# Double   ""

name = "Vimal"
print(name)

# Triple   """   - Multiline

name = """Harry
He is good person
....
...
...
etc"""
print(name)

# dir = "C:/omedir\some dir"  # SyntaxWarning: invalid escape sequence '\s'
# print(dir)

# dir = r'C:\omedir\some dir'  # r - Raw string
# print(dir)

# Format of string

first_name = "Vimal"
last_name = "Patel"

print(first_name + " " + last_name)
print(first_name, last_name)
# f- use for formating, and it will replace values of variables
# {} placeholders
print(f'Your First Name is: {first_name},Last Name is: {last_name}')
