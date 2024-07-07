# walk in dir

import os


for root, dir, files in os.walk("Users/ViMS/PycharmProjects/PyLearning/Ex_05072024"):
    print(f"Current dir : {root}")
    print(f"Sub dir : {dir}")
    print(len(files))