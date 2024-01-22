#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    j = 0
    while j + 1 != len(my_list):
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp
        j += 1
    return (my_list[len(my_list) - 1])
