limit = int(input())
i = 1
result = f'{i}'
jumlah = 1

while limit > jumlah:
    jumlah += i + 1
    i += 1
    result += f' + {i}'
print(f'The consecutive sum: {result} = {jumlah}')
