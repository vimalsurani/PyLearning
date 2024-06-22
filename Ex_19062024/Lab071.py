# List - Collection of items

num = [1, 2, 3]


def do_something(num_list):
    num_list.append(4)
    num_list[2] = 12
    return num_list


num.append(25)
list1 = do_something(num)
print(list1)
