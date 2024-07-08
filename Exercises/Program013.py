# Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

def check_num_divisible_by_five(num_list):
    print("Given List is :", num_list)

    for i in num_list:
        if i % 5 == 0:
            print(f'{i} is Divisible by 5')


check_num_divisible_by_five([10, 20, 30, 44, 52, 60])
