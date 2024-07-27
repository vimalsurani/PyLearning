# Write a program to check if the given file is empty or not
import os

size = os.stat('demo.txt').st_size

if size == 0:
    print("File Empty")
else:
    print("Not Empty")
