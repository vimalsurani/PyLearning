import os

file_name = os.open('testdata.txt',os.O_RDWR)
os.write(file_name,b'Hello i am writing here')
os.close(file_name)