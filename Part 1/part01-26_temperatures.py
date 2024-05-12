fahrenheit = int(input('Please type in a temperature (F):'))
celcius = float((fahrenheit - 32) / 1.8)
print(f'{fahrenheit} degrees Fahrenheit equals {celcius} degrees Celsius')
if celcius < 0:
    print("Brr! It's cold in here!")
    