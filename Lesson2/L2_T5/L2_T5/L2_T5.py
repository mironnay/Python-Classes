arr = [2148, 834, 441, 3312, 241]
arr_range = 5
i = 0
sum = 0

while i < arr_range:
    sum += arr[i]
    i += 1
    if i == 5:
        print("Sum: ", sum)