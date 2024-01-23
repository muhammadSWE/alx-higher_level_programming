#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            print(my_list[i], end="")
            n += 1
            for j in range(n):
                print("", end="")
        print()
        return n
    except IndexError:
        print()
        return n
