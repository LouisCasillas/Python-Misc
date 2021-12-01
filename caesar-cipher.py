def caesar_cipher(o_string, shift):
    # 65 - A
    # 97 - a

    cipher_text = ''

    for c in o_string:
        new_c = c

        if c.isalpha():
            if c.isupper():
                new_c = chr(65 + (((ord(c) - 65) + shift) % 26))
            else:
                new_c = chr(97 + (((ord(c) - 97) + shift) % 26))

        cipher_text += new_c

    return cipher_text

print(caesar_cipher('hello', 5))
print(caesar_cipher('hello', 26*29))
