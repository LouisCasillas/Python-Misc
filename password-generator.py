import random
import string

# input: number of characters for the password
# output: random password of X characters
def givePassword(password_length=8):

    possible_characters = list(string.ascii_letters + string.digits + string.punctuation + string.digits)

    return ''.join([random.choice(possible_characters) for i in range(password_length)])

how_many_characters = int(input("How many characters should the password be? "))

print(givePassword(how_many_characters))
