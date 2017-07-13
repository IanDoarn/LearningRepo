"""
Fibonacci sequence using python
generators

Written by: Ian Doarn
"""
def fib():
    # Generator that yields fibonacci numbers
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

if __name__ == '__main__':
    # Maximum fib numbers to print
    max_i = 20

    for i, fib_n in enumerate(fib()):

        #Print each yielded fib number
        print('{i:3}: {f:3}'.format(i=i, f=fib_n))

        # Break when we hit max_i value
        if i == max_i:
            break
