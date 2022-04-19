

def is_unique(arr):

    checker = 0

    for val in arr:

        print("val = {}".format(val))
        print("checker = {}".format(checker))

        if ((checker & (1 << val)) > 0):
            return False

        checker |= (1 << val);

    return True

x = [6, 7]

print("Is unique: {}".format(is_unique(x)))
