# OS Module
# Used to interact with operating system
# get working dir , change dir , file exist, fileName , sizeFile , Environment

import os

# print(os.name)
# nt - Window
# posix - Unix/Linux , mac

# print(os.getcwd())   # \Users\ViMS\PycharmProjects\PyLearning\Ex_05072024
#
# os.chdir("/Users/ViMS/PycharmProjects/PyLearning")
# print(os.getcwd())
# print(os.listdir("/Users/ViMS\PycharmProjects/PyLearning"))

# os.mkdir("Vimal")

size = os.path.getsize("testdata.txt")  # 22 bytes
print(size)

if size != 0:
    print("File exist and has content")
else:
    print("File not exist and no content")

m_time = os.path.getmtime("testdata.txt")  # float - it give - epoch time
print(m_time)

import time

print(time.gmtime(m_time))
print(time.localtime())
