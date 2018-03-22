from random import randint


def create_history(size=100):
    return [randint(0, 5) > 0 for _ in range(size)]


def is_flaky(value):
    return "is{} flaky.\nValue is {}\n".format(" not" * (value > 1), value)


def square(history=False):
    if not history:
        history = create_history()
    failure = 1
    success = 1
    previous = 2
    power = 0
    for h in history:
        if h == previous:
            power += 1
        else:
            power = 1
        previous = h
        if h:
            success += 4 ** power
        else:
            failure += 4 ** power
    return float(success) / failure


def diminishing(history=False):
    if not history:
        history = create_history()
    coefficient = 1
    success = 1
    failure = 1
    for h in history:
        if h:
            success += h * coefficient
        else:
            failure += h * coefficient
        coefficient *= .5
    return success / failure


def diminishing_square(history=False):
    if not history:
        history = create_history()
    coefficient = 1
    failure = 1
    success = 1
    previous = 2
    power = 0
    for h in history:
        if h == previous:
            power += 1
        else:
            power = 1
        previous = h
        if h:
            success += 4 ** (power * coefficient)
        else:
            failure += 4 ** (power * coefficient)
        coefficient *= .5
    return float(success) / failure


if __name__ == '__main__':
    history = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("square algorithm: {}".format(is_flaky(square(history))))
    print("diminishing algorithm: {}".format(is_flaky(diminishing(history))))
    print("combined algorithm: {}".format(is_flaky(diminishing_square(history))))
