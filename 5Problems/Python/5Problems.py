"""
Five programming problems every Software Engineer should be able to solve in less than 1 hour
http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

"""

from itertools import chain, zip_longest, permutations
from string import ascii_lowercase
import random

#==========
# Problem 1
#
# Write three functions that compute the sum of the
# numbers in a given list using a for-loop, a while-loop,
# and recursion.
#==========

P1_TEST_CASES =[
    [random.randint(0, 20) for a in range(0, 20)],
    [random.randint(0, 20) for b in range(0, 20)],
    [random.randint(0, 20) for c in range(0, 20)]
]

def sum_for(_list):
    a = 0
    for _, v in enumerate(_list):
        a += v
    return a

def sum_while(_list):
    a = 0
    while len(_list) > 0:
        a += _list[0]
        _list.pop(0)
    return a

def sum_recursive(_list):
    if len(_list) == 0:
        return 0
    else:
        return _list[0] + sum_recursive(_list[1:])

# if __name__ == '__main__':
#     for l in P1_TEST_CASES:
#         print("RECURSIVE :: {} = {}".format(str(l), str(sum_recursive(l))))
#     for l in P1_TEST_CASES:
#         print("FOR-LOOP :: {} = {}".format(str(l), str(sum_for(l))))
#     for l in P1_TEST_CASES:
#         print("WHILE-LOOP :: {} = {}".format(str(l), str(sum_while(l))))

#==========
# Problem 2
#
# Write a function that combines two lists by alternatingly
# taking elements. For example: given the two
# lists [a, b, c] and [1, 2, 3], the function should
# return [a, 1, b, 2, c, 3].
#==========

P2_TEST_CASES = [
    [[1,2,3],['a','b','c']],
    [['a','b','c'],['A','B','C']],
    [[i for i in range(1,27)],list(ascii_lowercase)]
]

def alternate(list1, list2):
    return [x for x in chain.from_iterable(zip_longest(list1, list2)) if x]

# if __name__ == '__main__':
#     for l in P2_TEST_CASES:
#         print('List 1: {}\nList 2: {}\nAlternating combinations: {}'.format(
#             str(l[0]), str(l[1]), str(alternate(l[0], l[1]))
#         ))

#==========
# Problem 3
#
# Write a function that computes the list of the first 100
# Fibonacci numbers. By definition, the first two numbers
# in the Fibonacci sequence are 0 and 1, and each subsequent
# number is the sum of the previous two. As an example,
# here are the first 10 Fibonnaci numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
#==========

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# if __name__ == '__main__':
#     l = []
#     for i, x in enumerate(fib()):
#         l.append(x)
#         if i >= 100:
#             break
#     print(l)

#==========
# Problem 4
#
# Write a function that given a list of non negative integers,
# arranges them such that they form the largest possible number.
# For example, given [50, 2, 1, 9], the largest formed number is 95021.
#==========
P3_TEST_CASES = [
    [random.randint(0, 10) for d in range(0, 10)],
    [random.randint(0, 10) for e in range(0, 10)],
    [random.randint(0, 10) for f in range(0, 10)]
]

def get_largest_possible_number(iterable):
    _set = set(permutations(iterable))
    return max([int(''.join([str(y) for y in list(x)])) for x in _set])

# if __name__ == '__main__':
#     for l in P3_TEST_CASES:
#         print(get_largest_possible_number(l))


#==========
# Problem 5
#
# Write a program that outputs all possibilities to put + or - or nothing
# between the numbers 1, 2, ..., 9 (in this order) such that the result
# is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
#==========

# TODO: Finish number 5!!