import random

def fill_list(some_list, list_lenth):
    i = 0 
    while i < list_lenth:
        some_list.append(random.randint(0, 100))
        i += 1

def print_pair_numbers(some_list):
    print("List`s pair numbers: ")
    for i in some_list:
        if i % 2 == 0:
            print(some_list[i], end = ", ")

my_list = list()

list_lenth = int(input("Enter lenth of the list: "))
fill_list(my_list, list_lenth)
print("List: \n" + str(my_list))
print_pair_numbers(my_list)