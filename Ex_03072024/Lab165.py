import csv

with open('TestData.csv') as csvfile:
    reader = csv.reader(csvfile)
    # for row in reader:
    #     print(row[0], row[1], sep=" | ")

    for col in reader:
        print(col[0], col[1], sep=" | ")
