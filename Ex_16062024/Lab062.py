# *args - any number of arguments
# print("Viaml", "Panth", "RT")


def sum(a=1, b=1, c=1):
    return a + b + c


# result = sum_three()
result1 = sum()
result2 = sum(1, 2)
result3 = sum(5, 7, 8)
result4 = sum(a=50, b=60, c=25)
result5 = sum(b=87, a=78, c=15)
print(result1, result2, result3, result4, result5)
