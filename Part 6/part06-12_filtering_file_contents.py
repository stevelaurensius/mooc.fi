# All the operations are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which:
# - Reads the contents of the file solutions.csv
# - writes those lines which have a correct result into the file correct.csv
# - writes those lines which have an incorrect result into the file incorrect.csv

def filter_solutions():
    with open('correct.csv', 'w') as correct:
        pass
    with open('incorrect.csv', 'w') as incorrect:
        pass
    with open('solutions.csv') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split(';')
            line = [int(item) if item.isdigit() else item for item in line]
            temp_container = []
            if '-' in line[1]:
                temp_container = line[1].split('-')
                temp_container = int(temp_container[0]) - int(temp_container[1])
            if '+' in line[1]:
                temp_container = line[1].split('+')
                temp_container = int(temp_container[0]) + int(temp_container[1])
            if temp_container == line[2]:
                with open('correct.csv', 'a') as correct:
                    correct.write(f'{line[0]};{line[1]};{line[2]}\n')
            else:
                with open('incorrect.csv', 'a') as incorrect:
                    incorrect.write(f'{line[0]};{line[1]};{line[2]}\n')
