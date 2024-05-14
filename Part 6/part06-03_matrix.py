# Please write two functions, named matrix_sum and matrix_max.
# Both go through the matrix in the file, and then return the sum of
# the elements or the element with the greatest value, as the names
# of the functions imply.

# Please also write the function row_sums, which returns a list
# containing the sum of each row in the matrix.

def matrix_sum():
    with open('matrix.txt') as file:
        result_list = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(',')
            line = [int(x) for x in line]
            result_list.append(sum(line))
    return sum(result_list)


def matrix_max():
    with open('matrix.txt') as file:
        result_list = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(',')
            line = [int(x) for x in line]
            result_list.append(max(line))
    return max(result_list)


def row_sums():
    with open('matrix.txt') as file:
        result_list = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(',')
            line = [int(x) for x in line]
            result_list.append(sum(line))
    return result_list


if __name__ == "__main__":
    row_sums()