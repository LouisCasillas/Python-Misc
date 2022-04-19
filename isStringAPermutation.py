def is_string_a_permutation(main_string, possible_permutation_string):
    main_list = list(main_string)
    possible_permutation_list = list(possible_permutation_string)

    main_list.sort()
    possible_permutation_list.sort()

    if main_list == possible_permutation_list:
        print('Yes')
    else:
        print('No')

is_string_a_permutation("hello","ellho")
is_string_a_permutation("hello","zebra")
