import math
from functools import reduce

import a as a


def q1(func_list: list) -> list:
    return list(filter((lambda x: x.__code__.co_argcount <= 1), func_list))


def q2(numbers: list = [1, 2, 3, 4]):
    print(reduce(lambda x, y: x + y, numbers))


def q3(number):
    return (lambda x: int(math.sqrt(x)) if (int(math.sqrt(x) + 0.5) ** 2 == x) else 0)(number)


def q4():
    sentences = ['Mary read a story to Sam and Isla.', 'Isla cuddled Sam.', 'Sam chortled.']
    sam_count = 0
    sam_count = sum(list(map(lambda str: str.count("Sam"), sentences)))
    print(sam_count)


avg_in = 0
avg_out = 0
funcs_amount = 0
returned_sum = 0


def q5(func):
    tup = []

    def wrapper(*args, **kwargs):
        number = args[0]
        answer = func(*args, **kwargs)
        if len(tup) == 0:
            tup.append(number)
            tup.append(answer)
        else:
            tup[0] = (tup[0] + number) / 2
            tup[1] = (tup[1] + answer) / 2
        tuple(tup)
        return tup

    # print("avarage argument :" + str(tup[0]) + '\n' + "avrage result" + str(tup[1]))

    return wrapper


@q5
def q51(x):
    return 1


@q5
def q52(x):
    return 2


@q5
def q53(x):
    return 3


def q5_b(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            args_len = len(args)
            numbers = args  # check name
            type_of_argument = 1
        elif len(kwargs) > 0:
            args_len = len(kwargs)
            numbers = kwargs
        else:
            print("wrong")
        if type_of_argument == 1:
            output_from_func = func(*args)
        else:
            output_from_func = func(*kwargs)
        print("func is ", func.__name__, "input  is ", numbers, " o utput is ", output_from_func)
        return ""

    return wrapper


@q5_b
def q5_b1(x, y):
    return 1


@q5_b
def q5_b2(x, y):
    return 2


@q5_b
def q5_b3(x, y):
    return 3


def q6(func):
    q6.funcs = []

    def wrapper(*args, **kwargs):
        func_list = q6.funcs
        if len(func_list) < 2:
            func_list.append(func.__name__)
        if len(func_list) >= 2:
            func_list.append(func.__name__)
            print(" 3 last functions that ran  :" + str(func_list))
            func_list.pop()
            return func(*args, **kwargs)

    return wrapper


@q6
def q61():
    return 1


@q6
def q62():
    return 2


@q6
def q63():
    return 3


@q6
def q64():
    return 4


# q7
class Twitter:
    def __init__(self, name):
        self.name = name
        self.subscribers = set()
        self.twits = list()

    def tweet(self, param):
        print('{} twitted this : \n{}'.format(self.name, param))
        self.twits.append(param)
        for t in self.subscribers:
            print('{} got twitt from {} : {}'.format(t.name, self.name, param))

    def follow(self, twitter):
        twitter.subscribers.add(self)
        return self


# q8
def f1(x, y=[]):
    # The first time it is called without the y arg
    # the default will work, but calls after that will update the existing y list
    y.append(x)
    return sum(y)


def f2(x, y=None):
    # each time we call this function without the y arg the y list will be created as new
    if y is None:
        y = []
    y.append(x)
    return sum(y)


class A:

    def __init__(self, y):
        self.y = y

    def __call__(self, z):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z


class B(A):
    def __call__(self, z=4):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z


def main():
    print(q1([lambda x: x + 1, lambda x, y: x + y, lambda x, t, y: 5, lambda z: z]))
    q2()
    print(q3(25))
    print(q3(26))
    q4()
    a1 = q51(5)
    a2 = q51(10)
    print("average argument :" + str(a1[0]) + '\n' + "average result" + str(a1[1]))
    print("average argument :" + str(a2[0]) + '\n' + "average result" + str(a2[1]))
    print(q5_b3(3, 4))
    print(q5_b3(3, 3))
    q61()
    q62()
    q63()
    q64()
    q64()
    # q7
    alice = Twitter('Alice')
    king = Twitter('King')
    queen = Twitter('Queen')
    hatter = Twitter('Mad Hatter')
    cat = Twitter('Cheshire Cat')
    alice.follow(cat).follow(hatter).follow(queen)
    king.follow(queen)
    queen.follow(queen).follow(hatter)
    hatter.follow(alice).follow(queen).follow(cat)

    print(f'==== {queen.name} tweets ====')
    queen.tweet('Off with their heads!')
    print(f'\n==== {alice.name} tweets ====')
    alice.tweet('What a strange world we live in.')
    print(f'\n==== {king.name} tweets ====')
    king.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
    print(f'\n==== {cat.name} tweets ====')
    cat.tweet("We're all mad here.")
    print(f'\n==== {hatter.name} tweets ====')
    hatter.tweet('Why is a raven like a writing-desk?')
    print(f1(10))
    print(f1(30))
    print(f2(10))
    print(f2(30))
    print(A(5)(B(6)()))
    print(A(6)(B(5)(6)))


if __name__ == "__main__":
    main()
