import math

inpt = str(input('Word: '))
inpt_length = len(inpt)
space_number = 30 - 2 - inpt_length
left_space = math.ceil(space_number / 2)
right_space = math.floor(space_number / 2)

print('*' * 30)
print('*' + (' ' * left_space) + inpt + (' ' * right_space) + '*')
print('*' * 30)
