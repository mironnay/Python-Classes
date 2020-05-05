import random

def fill_list(some_list = list(), list_start = 0, list_end = 100):
    for i in range(list_start, list_end):
        some_list.append(random.randint(0, 100))

def calc_list_summ(some_list = list()):
    sum = 0
    for i in range(0, len(some_list)):
        sum += some_list[i]
    return sum

my_list = list()

fill_list(my_list, 0, 10)
print("Generated list: \n" + str(my_list))
print("Sum: " + str(calc_list_summ(my_list)))
