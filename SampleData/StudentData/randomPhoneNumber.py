from random import randint


def random_US_phone_number():
    return  "{}{}{}-555-{}{}{}{}".format(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

if __name__ == '__main__':
    for _ in range(10):
        print(random_US_phone_number())