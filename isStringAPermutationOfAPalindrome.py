
from collections import Counter

def is_from_palindrome(test_string):

    test_alpha_only = [ c for c in test_string if c.isalpha() ]

    character_count = Counter(test_alpha_only)

    if len([v for v in character_count.values() if (v % 2) == 1]) > 1:
        print('No')
    else:
        print('Yes')


is_from_palindrome("tact coa")
is_from_palindrome("hello zebra")
