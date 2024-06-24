letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u

def vowel_func(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


# result  = filter_vowel('p')
# print(result)

filtered_list_words = filter(vowel_func, letters_list)
print(list(filtered_list_words))

filtered_tuple_words = filter(vowel_func, letters_tuple)
print(tuple(filtered_tuple_words))

filtered_set_words = filter(vowel_func, letters_set)
print(tuple(filtered_set_words))

