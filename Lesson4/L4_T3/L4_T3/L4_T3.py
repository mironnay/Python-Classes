import random

def fill_list(some_list, list_lenth):
    i = 0 
    while i < list_lenth:
        some_list.append(random.randint(1, 6))
        i += 1

my_list = list()
fill_list(my_list,100)
print(my_list)

my_dict = dict.fromkeys(my_list, 0)
for elem in my_list:
    if elem in my_dict.keys():
        my_dict[elem] += 1 
#print(my_dict)
moda = max(my_dict.values())
my_list.clear()

for key in my_dict:
    if my_dict[key] == moda:
        my_list.append(key)

print("The most popular number is " + str(max(my_list)))