from math import sqrt


def n_fib(n):
    n += 1
    return int(((1 + sqrt(5)) / 2) ** n / sqrt(5) + 0.5)


def numberwang(s):
    total = 0
    # python trick, booleans are actually integers.  0 is False, anything else is True
    fib = 0
    deuces = False
    if type(s) is not str:
        s = str(s)
    for character in s:
        if character in ("12"):
            fib += 1
            if character is "2":
                deuces = True
            else:
                deuces = False
        elif fib:
            if deuces and character in ("789"):
                total += 1
            else:
                total += 2
            total += n_fib(fib)
            fib = 0
            deuces = False
        else:
            total += 1
    if fib:
        total+= n_fib(fib)
    return(total)

SOLVE_ME = 9

print(numberwang(SOLVE_ME))
