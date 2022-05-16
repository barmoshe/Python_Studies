import time

"""
Q1
<R>:- <P> | <C> | <P>S | <C>S
<C>:- EEF | EE <EEF> F | EF <EEF> | EFE | E<EEF>EF | <EF<EEF>E | <C><C>
<P>:- EF | E <EF> F | EF <EF> | <P> <P>
<EEF>:- ε | EEF| EFE| FEE | EE<EEF>F | F<EEF>EE | E<EEF>FE | E<EEF> EF | EF<EEF>E <EF>:-ε | EF| FE| E<EF>F | F<EF>E
"""
# funcs
def sum_int_list(num_list):
    return sum(num_list)


def list_sum(list_of_lists):
    sum1 = 0
    for x in list_of_lists:
        sum1 += sum_int_list(x)
    return sum1


def reverse_string_tuples(s):
    s = s[::-1]
    return s


def reverse_list_of_list(list1):
    list1 = list(reversed(list1))
    i = 0
    for x in list1:
        list1[i] = list(reversed(x))
        i += 1
    return list1


def reverse_tuple(tup1):
    return reverse_string_tuples(tup1)


def put_chars_from_set(current_set, char_tup):
    result_tuple = tuple()
    for x in current_set:
        if type(x) == str and x not in char_tup:
            result_tuple = result_tuple + (x,)
    return result_tuple


def put_nums_from_set(current_set, num_tup):
    result_tuple = tuple()
    for num in current_set:
        if (isinstance(num, int) or isinstance(num, float)) and num not in num_tup:
            result_tuple = result_tuple + (num,)
    return result_tuple


def organize_tuple_of_sets(tup_of_sets):
    num_tup = tuple()
    char_tup = tuple()
    for current_set in tup_of_sets:
        if set == type(current_set):
            char_tup = char_tup + put_chars_from_set(current_set, char_tup)
            num_tup = num_tup + put_nums_from_set(current_set, num_tup)
    num_tup = sorted(num_tup)
    char_tup = sorted(char_tup)
    result_tup = char_tup + num_tup
    return result_tup

def sort_tuples(tuples_q4):
    new_list = []
    new_list1 = set()
    for x in tuples_q4:
        for y in x:
            if type(y) == str:
                new_list.append(y)
        new_list.sort()
    for x in tuples_q4:
        for y in x:
            if type(y) != str:
                new_list1.add(y)
    new_list1 = sorted(new_list1)
    for x in new_list1:
        new_list.append(x)
    return new_list


def sort_tuples_dictionary(tuples_q4_b):
    dict1 = {}
    y = 0
    for x in sort_tuples(tuples_q4_b):
        dict1[y] = x
        y = y + 1
    return dict1
def organize_tuple_of_sets_dictionary(tup_of_sets):
    tup_of_sets = organize_tuple_of_sets(tup_of_sets)
    result_dic = {}
    i = 0
    for element in tup_of_sets:
        result_dic[i] = element
        i = i+1
    return result_dic


# start tests
def test_list_of_list_sum():
    list1 = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
    assert (list_sum(list1) == 45)
    list1 = [{1, -2, 3}, {4, 5, 6}, {7, 8, 9}]
    assert (list_sum(list1) == 41)
    list1 = [{-1, -2, -3}, {-4, -5, -6}, {-7, -8, -9}]
    assert (list_sum(list1) == -45)


def test_reverse():
    assert (reverse_string_tuples("hello") == "olleh")


def test_reverse_list_of_list():
    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list2 = reverse_list_of_list(list1)
    assert (list2 == [[9, 8, 7], [6, 5, 4], [3, 2, 1]])


def test_reverse_tuple():
    tup1 = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
    tup_rev = ('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
    assert (tup_rev == reverse_tuple(tup1))


def test_organize_tuple_of_sets():
    # A
    answer = organize_tuple_of_sets(({2, 4, 3}, {'f', 'h', 'u', 'r', 'b', 'n', 'd'}))
    assert (answer == ['b', 'd', 'f', 'h', 'n', 'r', 'u', 2, 3, 4])
    answer = organize_tuple_of_sets(({2, 4, 3, 'g', 'd'}, {'f', 'h', 'u', 1, 3, 4}))
    assert (answer == ['d', 'f', 'g', 'h', 'u', 1, 2, 3, 4])
    # B
    answer = organize_tuple_of_sets_dictionary(({2, 4, 3, 'g', 'd'}, {'f', 'h', 'u', 1, 3, 4}))
    assert (answer == {0: 'd', 1: 'f', 2: 'g', 3: 'h', 4: 'u', 5: 1, 6: 2, 7: 3, 8: 4})
    answer = organize_tuple_of_sets_dictionary(({2, 1.3, 3, 'g', 'd'}, {4.6, 2, 'h', 'A', 1, 3}))
    assert (answer == {0: 'A', 1: 'd', 2: 'g', 3: 'h', 4: 1, 5: 1.3, 6: 2, 7: 3, 8: 4.6})


# end alert
def end_test():
    print("calculating")
    time.sleep(0.15)
    print("   ...   ")
    time.sleep(0.33)
    print("   ...   ")
    time.sleep(0.49)
    print("   ...   ")
    time.sleep(0.7)
    print("passed text")


if __name__ == '__main__':
    test_list_of_list_sum()
    test_reverse()
    test_reverse_list_of_list()
    test_reverse_tuple()
    test_organize_tuple_of_sets()
    end_test()
