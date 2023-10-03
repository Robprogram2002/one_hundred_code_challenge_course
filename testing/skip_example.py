import unittest
import sys

mylib_version = 2


def external_resource_available():
    return False


# Classes can be skipped just like methods:
# @unittest.skip("showing class skipping")
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib_version < 3,
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            # we can use this same function in the TestCase.setUp()
            # This is useful when a resource that needs to be set up is not available.
            self.skipTest("external resource not available")
            # test code that depends on the external resource
        pass

    # Expected failures use the expectedFailure() decorator.
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


if __name__ == '__main__':
    unittest.main()
