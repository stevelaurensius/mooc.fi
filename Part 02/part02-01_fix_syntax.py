number = int(input("Please type in a number: "))
if number>100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now" + " " + str(number))
print(str(number) + "" + " must be my lucky number!")
print("Have a nice day!")
