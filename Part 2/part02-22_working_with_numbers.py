counter = 0
jumlah = 0
daftar = []
print('Please type in integer numbers. Type in 0 to finish.')
while True:
    entry = int(input('Number'))
    jumlah += entry
    if entry == 0:
        break
    daftar.append(entry)
    counter += 1
print(f'Numbers typed in {counter}')
print(f'The sum of the numbers is {jumlah}')
rata_rata = round(jumlah / counter, 1)
print(f'The mean of the numbers is {rata_rata}')
positive_count = 0
for number in daftar:
    if number > 0:
        positive_count += 1
print(f'Positive numbers {positive_count}')

negative_count = 0
for number in daftar:
    if number < 0:
        negative_count += 1
print(f'Negative numbers {negative_count}')
