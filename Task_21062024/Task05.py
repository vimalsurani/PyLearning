# Anagrams

# String s1 = "silent";#
# String s2 = "listen";

# namo - mano - onam

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase


def check_anagram(str_s1, str_s2):
    if sorted(str_s1) == sorted(str_s2):
        print(f"The strings {str_s1} and {str_s2} are anagrams.")
    else:
        print(f"The strings {str_s1} and {str_s2} aren't anagrams.")

    # driver code


check_anagram("silent", "listen")
