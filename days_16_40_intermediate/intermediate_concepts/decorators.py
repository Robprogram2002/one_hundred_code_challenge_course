import functools


# ****************** THEORY
# In order to understand about decorators, we must first know a few basic things in Python. We must be comfortable
# with the fact that everything in Python (Yes! Even classes), are objects. Names that we define are simply
# identifiers bound to these objects. Various different names can be bound to the same function object.

def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")


# When you run the code, both functions first and second give the same output. Here, the names first and
# second refer to the same function object.

# Functions can be passed as arguments to another function.
# Such functions that take other functions as arguments are also called higher order functions.
# Furthermore, a function can return another function.

def is_called():
    def is_returned():
        print("Hello")

    return is_returned


new = is_called()

# Outputs "Hello"
new()


# Functions and methods are called callable as they can be called.
# In fact, any object which implements the special __call__() method is termed callable. So, in the most basic sense,
# a decorator is a callable that returns a callable.
# Basically, a decorator takes in a function, adds some functionality and returns it.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


ordinary()
pretty = make_pretty(ordinary)
pretty()


# In the example shown above, make_pretty() is a decorator. In the assignment step:  pretty = make_pretty(ordinary)
# The function ordinary() got decorated and the returned function was given the name pretty.
# Generally, we decorate a function and reassign it as,
# ordinary = make_pretty(ordinary).

# This is a common construct and for this reason, Python has a syntax to simplify this. We can use the @ symbol
# along with the name of the decorator function and place it above the definition of the function to be decorated.
# For example,

@make_pretty
def ordinary():
    print("I am ordinary")  # is equivalent to


def ordinary():
    print("I am ordinary")


ordinary = make_pretty(ordinary)


# Decorators with parameters
def divide(a, b):
    return a / b


# This function has two parameters, a and b. We know it will give an error if we pass in b as 0.
# Now let's make a decorator to check for this case that will cause the error.
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


# In this manner, we can decorate functions that take parameters.

# A keen observer will notice that parameters of the nested inner() function inside the decorator is the same as
# the parameters of functions it decorates. Taking this into account, now we can make general decorators that work with
# any number of parameters.

# In Python, this magic is done as function(*args, **kwargs). In this way, args will be the tuple of positional
# arguments and kwargs will be the dictionary of keyword arguments. An example of such a decorator will be:

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)

    return inner


# Changing Decorators

# Multiple decorators can be chained in Python.

# This is to say, a function can be decorated multiple times with different (or same) decorators. We simply place
# the decorators above the desired function.

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")


# is equivalent to
def printer(msg):
    print(msg)


printer = star(percent(printer))


# ***************** FUNCTION DECORATORS

# simple decorator template -> decorator without parameters
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before....
        print("before")
        result = func(*args, **kwargs)
        print(result)
        # Do something after ....
        print("after")
        return result

    return wrapper


@my_decorator
def add_five(x):
    return x + 5


# add_five = my_decorator(add_five(x))   this is the result of apply a decorator
print(add_five(8))

print("")
print("")


# decorator template with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
                print(result)
            print(result)
            return result

        return wrapper

    return decorator_repeat


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("before the repeat decorator")
        result = func(*args, **kwargs)
        print("after the  repeat decorator and the original function")
        return result

    return wrapper


# if we use multiple decorators, they are executed in order from top to bottom
@start_end_decorator
@repeat(num_times=4)
def greetings(name):
    return f"hello {name}"


greetings("Robert")

# ***************** CLASS DECORATORS
