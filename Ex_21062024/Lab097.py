vimal_details = \
    {"name": "vimal",
     "90": 34.34,
     "isMale": True,
     "Address": "GJ"
     }

print(vimal_details.get("Address"))
print(vimal_details["Address"])
print(vimal_details.values())
print(vimal_details.keys())

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95, 'd': 95}
print(my_dict)
print(len(my_dict))
print("Key:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))

# for i in list(my_dict.values()):
#     print(i)


for k, v in my_dict.items():
    print(k, v)
