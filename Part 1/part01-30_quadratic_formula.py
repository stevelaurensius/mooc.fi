from math import sqrt

a = int(input('Value of a: '))
b = int(input('Value of b: '))
c = int(input('Value of c: '))


discriminant = b ** 2 - (4 * a * c)

sol1 = (- b - sqrt(discriminant)) / (2 * a)
sol2 = (- b + sqrt(discriminant)) / (2 * a)

print(f'The roots are {sol2} and {sol1}')
