import random

def fill_list(some_list, list_lenth = 10):
    i = 0 
    while i < list_lenth:
        some_list.append(random.randint(0, 100))
        i += 1

def calc_list_summ(some_list ):
    sum = 0
    for i in some_list:
        sum += i
    return sum

my_list = list()

fill_list(my_list)
print("Generated list: \n" + str(my_list))
print("Sum: " + str(calc_list_summ(my_list)))
