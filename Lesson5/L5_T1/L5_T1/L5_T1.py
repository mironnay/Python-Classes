file_read = open("L5_T1.py", 'r')
file_copy = open("script_copy.txt", 'w')

file_copy.write(file_read.read())

file_read.close()
file_copy.close()