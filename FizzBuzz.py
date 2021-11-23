# Print the numbers 1 to 100, one number per line.
#  - If the number is divisible by 3, print 'Fizz' rather than the number.
#  - If the number is divisible by 5, print 'Buzz' rather than the number.
#  - If the number is divisible by 3 and 5, print 'FizzBuzz' rather than the number.

def fizzBuzz(max_number=100):
    for i in range(1, max_number + 1):
        if (i % 15) == 0:
            print("FizzBuzz")
        elif (i % 5) == 0:
            print("Buzz")
        elif (i % 3) == 0:
            print("Fizz")
        else:
            print(i)

def fizzBuzz2(max_number=100):
    for i in range(1, max_number + 1):
        matches = 0

        if (i % 3) == 0:
            print("Fizz", end='')
            matches = 1
        if (i % 5) == 0:
            print("Buzz", end='')
            matches = 1

        if not matches:
            print(i)
        else:
            print('')

fizzBuzz()
