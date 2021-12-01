def caesar_cipher(o_string, shift):
    # 65 - A
    # 97 - a

    cipher_text = ''

    for c in o_string:
        new_c = c

        if c.isalpha():
            alphabet_ascii_start = 97

            if c.isupper():
                alphabet_ascii_start = 65

            new_c = chr(alphabet_ascii_start + (((ord(c) - alphabet_ascii_start) + shift) % 26))

        cipher_text += new_c

    return cipher_text

print(caesar_cipher('hello', 5))
print(caesar_cipher('hello', 26*29))

print(caesar_cipher(caesar_cipher('hello', 5), -5))
print(caesar_cipher('hello', -1 * (26*29)))
