user_line = input("Enter some number. I`ll calculate sum of all digits: ").strip()

while user_line.isnumeric() == False:
    user_line = input("Wrong format. Try again ").strip()
sum = 0

for i in user_line:
    sum += int(i)
print(sum)