def sun_func(a, b, c):
    # print(a, b, c)
    return a + b + c
    # print("This code will be never executed")


print("End")

# result1 = sun_func(3, 4, 5)
# result2 = sun_func(a=4, b=6, c=9)
# result3 = sun_func(b=6, a=4, c=9)
result4 = sun_func(1, 2, 3)
# result5 = sun_func()            # TypeError: sun_func() missing 3 required positional arguments: 'a', 'b', and 'c'
# print(sun_func(5,5,8))
print(result4)
