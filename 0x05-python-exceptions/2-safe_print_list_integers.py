afe_print_list_integers(my_list=[], x=0):
    idx = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            idx += 1

        except (ValueError, TypeError):
            continue

    print()
    return idx