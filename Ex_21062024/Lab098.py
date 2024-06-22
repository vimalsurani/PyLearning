# my_dict = {'b': 2, 'w': 1, 'c': 45, 'c': 35}
# print(my_dict)
#
# for k, v in my_dict.items():
#     print(k, v)
#
# from collections import OrderedDict
#
# od = OrderedDict()
# od['a'] = 45
# od['c'] = 78
# od['b'] = 97
# od['d'] = 31
# print(od)

# Dict - It will not keep the order of insertion
# OrderDict - It will keep the order of insertion

my_dict = dict()
my_dict['z'] = 45
my_dict['b'] = 12
my_dict['w'] = 32
my_dict['c'] = 11
my_dict['d'] = 19
print(my_dict)

for k, v in my_dict.items():
    print(k, v)
