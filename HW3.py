import math
from functools import reduce


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

if __name__ == "__main__":
    main()
