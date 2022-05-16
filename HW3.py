from functools import reduce


def q1(func_list: list) -> list:
    return list(filter((lambda x: x.__code__.co_argcount <= 1), func_list))


def q2(numbers: list = [1, 2, 3, 4]):
    print(reduce(lambda x, y: x + y, numbers))


def main():
    print(q1([lambda x: x + 1, lambda x, y: x + y, lambda x, t, y: 5, lambda z: z]))
    q2()


if __name__ == "__main__":
    main()
