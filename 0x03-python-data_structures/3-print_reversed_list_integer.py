#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_lst = my_list[::-1]
    for i in range(len(rev_lst)):
        print("{:d}".format(rev_lst[i]))
