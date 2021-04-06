while True:
    lower, upper, digit, space = 0,0,0,0
    try:
        sen = input()
        for i in sen:
            if i.islower(): lower += 1
            elif i.isupper(): upper += 1
            elif i.isdigit(): digit += 1
            elif i.isspace(): space += 1
        print(lower, upper, digit, space)
    except EOFError:
        break
