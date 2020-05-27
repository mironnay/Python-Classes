import time
file = open("logs.txt", 'a')

def decorator(func):
    def wrapper():
        file.write(str(time.ctime()) + " : " + str(func()) + '\n')
    return wrapper

def func1():
    return 123

def func2():
    return "hello"

