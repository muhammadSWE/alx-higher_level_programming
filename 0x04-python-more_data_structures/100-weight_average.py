#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    s = 0
    s_weight = 0
    for i in my_list:
        s += i[0] * i[1]
        s_weight += i[1]
    return s / s_weight
