from random import randint


def create_history(size=100):
    return [randint(0,5) > 0 for x in range(size)]


def is_flaky(value):
    return value < 1


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
            success += 2 ** power
        else:
            failure += 2 ** power
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
        coefficient *= .75
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
            success += 2 ** (power * coefficient)
        else:
            failure += 2 ** (power * coefficient)
        coefficient *= .75
    return success / failure


if __name__ == '__main__':
    history = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("square algorithm: {}".format(square(history)))
    print("diminishing algorithm: {}".format(diminishing(history)))
    print("combined algorithm: {}".format(diminishing_square(history)))
