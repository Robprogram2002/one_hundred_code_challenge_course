from typing import Union
import unittest

num = Union[int, float]


def _sum_recursively(numbers: [num], start=0) -> num:
    if start == len(numbers) - 1:
        return numbers[start]
    else:
        return numbers[start] + _sum_recursively(numbers, start + 1)


def sum_sequence(numbers: [num]) -> num:
    if len(numbers) == 0:
        return 0
    elif not isinstance(numbers[0], (int, float)):
        raise TypeError('elements of the sequence must be numbers')
    else:
        return _sum_recursively(numbers)


# A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.
# unittest provides a base class, TestCase, which may be used to create new test cases.

class TestSequenceSum(unittest.TestCase):

    def test_empty(self):
        testcase = []
        expected = 0
        self.assertEqual(sum_sequence(testcase), expected)

    def test_single(self):
        testcase = [10]
        expected = 10
        self.assertEqual(sum_sequence(testcase), expected)

    def test_general(self):
        testcase = [2, 18, 14, 45, -23, 4]
        expected = 60
        self.assertEqual(sum_sequence(testcase), expected)

    def test_invalid(self):
        self.assertRaises(TypeError, sum_sequence, ['a', 'b', 'c', 'd'])


# simple way to run the tests. unittest.main() provides a command-line interface to the test script. When run from the
# command line, the above script produces an output.
# Passing the -v option to your test script will instruct unittest.main() to enable a higher level of verbosity, and
# produce the following output

if __name__ == '__main__':
    unittest.main()



