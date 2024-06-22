# Unpacking of tuple
a, b, c = (10, 20, 30)

t = (50, 60, 70)
# t.append()  # tuple - immutable in nature
new_t = t+(80,)
print(new_t)

my_list = list(new_t)
print(my_list)
my_list.append(90)
new_t2 = tuple(my_list)
print(new_t2)