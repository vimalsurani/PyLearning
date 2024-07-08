def palindrome_num(num):
    print("Original number is :", num)
    original_num = num

    rev_num = 0
    while num > 0:
        rem = num % 10
        rev_num = (rev_num * 10) + rem
        num = num // 10

    if original_num == rev_num:
        print("Given number is palindrome")
    else:
        print("Given number is not palindrome")


palindrome_num(121)
