line_user = input("Type some words devided by coma: ")

line_list = line_user.split(",")
idx = 0
for i in line_list:
    line_list[idx] = str(i).strip()
    idx += 1

print(line_list)