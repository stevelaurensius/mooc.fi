gift = int(input('Value of gift:'))
result = 0

if gift < 5000:
    print('No Tax!')
if gift >= 5000:
    if 5000 <= gift <= 25000:
        result = 100 + (gift - 5000) * 0.08
        print(f'Amount of tax: {round(result, 1)} euros')
    if 25000 <= gift <= 55000:
        result = 1700 + (gift - 25000) * 0.1
        print(f'Amount of tax: {round(result, 1)} euros')
    if 55000 <= gift <= 200000:
        result = 4700 + (gift - 55000) * 0.12
        print(f'Amount of tax: {round(result, 1)} euros')
    if 200000 <= gift <= 1000000:
        result = 22100 + (gift - 200000) * 0.15
        print(f'Amount of tax: {round(result, 1)} euros')
    if gift >= 1000000:
        result = 142100 + (gift - 1000000) * 0.17
        print(f'Amount of tax: {round(result, 1)} euros')
