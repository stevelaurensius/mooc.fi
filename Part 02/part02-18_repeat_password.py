password = input('Password:')
while True:
    repeat_pass = input('Repeat password:')
    if password == repeat_pass:
        break
    print('They do not match!')
print('User account created!')
