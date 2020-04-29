num = input("Enter some number(meters): ")
convert = input("Enter some of the following (mm,cm,km): ")

if convert == "mm":
    print("Converted value is: ", int(num) * 1000)
elif convert == "cm":
    print("Converted value is: ", int(num) * 100)
elif convert == "km":
    print("Converted value is: ", int(num) / 1000)
else:
    print("Wrong format")