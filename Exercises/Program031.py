# Write all content of a given file into a new file by skipping line number 5

import os
try:
    with open('C:/Users/ViMS/PycharmProjects/PyLearning/Exercises/test.txt', 'r') as fp:
        lines = fp.readlines()

    with open('new_text.txt', 'w') as fp:
        counter = 0
        for line in lines:
            if counter == 4:
                counter = counter + 1
                continue
            else:
                fp.write(line)
            counter = counter + 1
finally:
    fp.close()