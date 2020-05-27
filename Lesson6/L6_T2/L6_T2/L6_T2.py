import random
import string 

file = open("somepasswords.txt",'a')

lenth = 30
password = ""
line = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

i = 0
while i < lenth:
    password += random.choice(line)
    i += 1
file.write(password + '\n')
file.close()