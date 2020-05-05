import random, math

def compare_nums(num1, num2):
    if num1 == num2 or abs(num1 - num2) == 5 or (num1 + num2) == 5:
        return True
    else:
        return False

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

print(str(num1) + " " + str(num2))
print(compare_nums(num1, num2))