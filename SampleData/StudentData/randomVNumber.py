from random import randint


def random_VNumber():
    return "V{}{}{}{}{}{}{}{}".format(*[randint(0, 9) for _ in range(9)])