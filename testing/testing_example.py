import unittest


# You can place the definitions of test cases and test suites in the same modules as the code they are to test
# (such as widget.py), but there are several advantages to placing the test code in a separate module

class Widget:
    def __init__(self, name, height=50, long=50):
        self._name = name
        self._height = height
        self._long = long

    def size(self):
        return self._height, self._long

    def resize(self, new_height, new_long):
        self._height = new_height
        self._long = new_long

    def dispose(self):
        print('bye!!')


# The order in which the various tests will be run is determined by sorting the test method names with respect to the
# built-in ordering for strings.

# If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')


# if __name__ == '__main__':
#     unittest.main()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
