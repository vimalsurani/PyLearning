# *args - any number of arguments
# print("Vimal", "Panth", "Rihan")


def sum_func(a=1, b=1, c=1):
    return a + b + c


result1 = sum_func()
result2 = sum_func(1, 2)
result3 = sum_func(5, 7, 8)
result4 = sum_func(a=50, b=60, c=25)
result5 = sum_func(b=87, a=78, c=15)
print(result1, result2, result3, result4, result5, sep="\n")
