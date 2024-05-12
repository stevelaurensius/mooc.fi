prev_code = ""
codes = ""

while True:
    code = input("Please type in a word:")
    if code == 'end' or code == prev_code:
        break
    codes += code + ' '
    prev_code = code

print(codes)
