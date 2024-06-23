student = int(input('How many students on the course?'))
group = int(input('Desired group size?'))
result = student // group
if result * group != student:
    result += 1
print(f'Number of groups formed: {result}')
