# File IO
import os.path

# with open('vimal.txt', 'r') as file:
#     print(file.read())
#     file.close()

try:
    file = open('vima.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("I am not able to find the file, Please check Path")
finally:
    print("Executed")
    try:
        file.close()  # Close has to be executed
    except NameError as ne:
        print(ne)
