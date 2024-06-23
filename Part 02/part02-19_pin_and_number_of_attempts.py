attempt = 0
while True:
    correct_pin = 4321
    pin = int(input('PIN'))
    attempt += 1

    if pin != correct_pin:
        print('Wrong')

    if pin == correct_pin:
        break

if attempt == 1:
    print('Correct! It only took you one single attempt!')
if attempt > 1:
    print(f'Correct! It took you {attempt} attempts')
    