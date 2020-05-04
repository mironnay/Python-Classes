import random

def fill_list(some_list = list(), list_start = 0, list_end = 100):
    for i in range(list_start, list_end):
        some_list.append(random.randint(0, 100))

def print_pair_numbers(some_list = list()):
    print("List`s pair numbers: ")
    i = 0
    for i in range(0, len(some_list)):
        if some_list[i] % 2 == 0:
            print(some_list[i], end = ", ")

list_lenth = 0
my_list = list()

list_lenth = int(input("Enter lenth of the list: "))
fill_list(my_list, 0, list_lenth)
#print("List: \n" + str(my_list))
print_pair_numbers(my_list)