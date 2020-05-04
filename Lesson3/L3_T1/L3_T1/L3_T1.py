import random
try_curr = 1
try_num = 4
range_bottom, range_celling = 0, 100
sys_num = random.randint(range_bottom, range_celling)
user_num = 0
if_true = False

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

def compare_numbers(user, program): #returns if numbers are same
    if program == user:
        print("Great! You have guessed right ")
        return True
    elif program < user:
        print("Your number is greater than mine ")
        return False
    elif program > user:
        print("Your number is lesser than mine ")
        return False

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

def return_num_tries(current, overal):
        if current <= overal:
            print(str(overal - current) + " tries left \n")
        elif current > overal:
            print("No tries left ")

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

#                               # executing program #               #

print("Try to guess my number. It is in range: " + str(range_bottom) + ", " + str(range_celling))

while try_curr <= try_num:
    if if_true == False:
        user_num = int(input("So, your number is: "))
        if_true = compare_numbers(user_num, sys_num)
    else:
        break
    return_num_tries(try_curr, try_num)
    try_curr += 1

print("Game over. My number is " + str(sys_num))
