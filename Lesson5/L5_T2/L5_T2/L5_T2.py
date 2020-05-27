import time
file = open("text_log.txt", 'a')

print("Hello! I`ll note everything you write into one file. Type 'E_N_D_' to exit.")
while True:
    user_ans = input("Waiting for input: ")
    if user_ans == "E_N_D_":
        break
    else:
        file.write(str(time.ctime()) + " : " + str(user_ans) + '\n')

file.close()
