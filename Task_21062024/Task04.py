# Count vowels and consonants in a String

str_name = "Vimal"


def count_vowels_and_consonants():
    vowels_str = "aeiouAEIOU"
    vow_count = 0
    cons_count = 0

    for char in str_name:
        if char.isalpha():
            if char in vowels_str:
                vow_count = vow_count + 1
            else:
                cons_count = cons_count + 1

    return vow_count, cons_count


vowels, consonants = count_vowels_and_consonants()
print(f"Vowels: {vowels}, Consonants: {consonants}")
