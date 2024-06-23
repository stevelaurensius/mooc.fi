age = int(input('What is your age?'))
if age < 0:
    print('That must be a mistake')
elif 5 > age >= 0:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")
    