import sys


# Python generators are a simple way of creating iterators.
# Simply speaking, a generator is a function that returns an object (iterator)
# which we can iterate over (one value at a time).

# It is fairly simple to create a generator in Python. It is as easy as defining a normal function,
# but with a yield statement instead of a return statement.
# If a function contains at least one yield statement (it may contain other yield or return statements), it
# becomes a generator function. Both yield and return will return some value from a function.
# The difference is that while a return statement terminates a function entirely, yield statement pauses the
# function saving all its states and later continues from there on successive calls

# When called, it returns an object (iterator) but does not start execution immediately. Methods like
# __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().

# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# It returns an object but does not start execution immediately.
a = my_gen()

next(a)

next(a)

next(a)


# next(a)


# One interesting thing to note in the above example is that the value of variable n is remembered between each call.
# Unlike normal functions, the local variables are not destroyed when the function yields. Furthermore, the generator
# object can be iterated only once.

# One final thing to note is that we can use generators with for loops directly.
# This is because a for loop takes an iterator and iterates over it using next() function.
# It automatically ends when StopIteration is raised.

# Normally, generator functions are implemented with a loop having a suitable terminating condition.


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

# ************ GENERATOR EXPRESSIONS
# Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.
# Similar to the lambda functions which create anonymous functions, generator expressions create
# anonymous generator functions. The syntax for generator expression is similar to that of a list
# comprehension in Python. But the square brackets are replaced with round parentheses.
# The major difference between a list comprehension and a generator expression is that a list comprehension produces
# the entire list while the generator expression produces one item at a time.

# They have lazy execution ( producing items only when asked for ). For this reason, a generator expression is
# much more memory efficient than an equivalent list comprehension.


my_list = [1, 3, 6, 10]

list_ = [x ** 2 for x in my_list]

generator = (x ** 2 for x in my_list)

print(list_)
print(generator)

# the generator expression did not produce the required result immediately. Instead, it returned a generator object,
# which produces items only on demand.

print(next(generator))

print(next(generator))

print(next(generator))

print(next(generator))

# next(generator)

# Generator expressions can be used as function arguments. When used in such a way, the round parentheses can be dropped

print(sum(x ** 2 for x in my_list))


# A normal function to return a sequence will create the entire sequence in memory before returning the result.
# This is an overkill, if the number of items in the sequence is very large. Generator implementation of such sequences
# is memory friendly and is preferred since it only produces one item at a time.

# Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.
# Suppose we have a generator that produces the numbers in the Fibonacci series. And we have another
# generator for squaring numbers. If we want to find out the sum of squares of numbers in the Fibonacci series,
# we can do it in the following way by pipelining the output of generator functions together.

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))


# comparison between creating a list or creating a generator
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(first_n(10000)))
print(sys.getsizeof(firstn_generator(10000)))

my_list = [i for i in range(10000) if i % 2 == 0]
my_generator = (i for i in range(10000) if i % 2 == 0)

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_generator))

