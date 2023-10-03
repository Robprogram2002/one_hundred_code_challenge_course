# A function defined inside another function is called a nested function. Nested functions can access
# variables of the enclosing scope.
# In Python, these non-local variables are read-only by default and we must declare them explicitly as non-local
# (using nonlocal keyword) in order to modify them.
# Following is an example of a nested function accessing a non-local variable.

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()


# Output: Hello
print_msg("Hello")


# In the example above, what would happen if the last line of the function print_msg()
# returned the printer() function instead of calling it?


def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Output: Hello
another = print_msg("Hello")
another()

# On calling another(), the message was still remembered although we had already finished executing
# the print_msg() function. This technique by which some data ("Hello in this case) gets attached to the
# code is called closure in Python. This value in the enclosing scope is remembered even when the variable goes out of
# scope or the function itself is removed from the current namespace.

# The criteria that must be met to create closure in Python are summarized in the following points.

# We must have a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.