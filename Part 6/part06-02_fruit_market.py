# Please write a function named read_fruits, which reads the file and
# returns a dictionary based on the contents. In the dictionary, the
# name of the fruit should be the key, and the value should be its
# price. Prices should be of type float.

def read_fruits():
    with open("fruits.csv") as file:
        result_dict = {}
        for line in file:
            line = line.replace("\n", "")
            line = line.split(';')
            result_dict[line[0]] = float(line[1])
    return result_dict
