line = input("Enter some words separated with SPACE, I`ll find the longest: ")

my_list = line.split(" ")
#print(my_list)

my_dict = dict.fromkeys(my_list, 0)
for elem in my_list:
    my_dict[elem] = len(elem)
#print(my_dict)
moda = max(my_dict.values())
my_list.clear()

for key in my_dict:
    if my_dict[key] == moda:
        my_list.append(key)

print("The longest word is " + max(my_list))