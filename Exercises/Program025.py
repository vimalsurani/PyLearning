# Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp


# base = 2
# exponent = 5
# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)


# def exponent(base, exp):
#     result = base ** exp
#     print(base, "raises to the power of", exp, "is: ", result)
#
#
# exponent(2, 5)


# def exponent(base, exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is: ", result)
#
#
# exponent(2, 4)


def exponent(base, exp):
    result = 1
    for i in range(exp):
        result = result * base
    print(base, "raises to the power of", exp, "is: ", result)


exponent(2, 4)
