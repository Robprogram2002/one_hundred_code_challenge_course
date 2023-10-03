### Organizing test code

The basic building blocks of unit testing are test cases — single scenarios that must be set up and checked for
correctness. In unittest, test cases are represented by ` unittest.TestCase` instances. To make your own test cases you
must write subclasses of TestCase or use FunctionTestCase.

The testing code of a TestCase instance should be entirely self-contained, such that it can be run either in isolation
or in arbitrary combination with any number of other test cases.

The simplest TestCase subclass will simply implement a test method (i.e. a method whose name starts with test) in order
to perform specific testing code.

in order to test something, we use one of the `assert*()` methods provided by the TestCase base class. If the test
fails, an exception will be raised with an explanatory message, and unittest will identify the test case as a failure.
Any other exceptions will be treated as errors.

Tests can be numerous, and their set-up can be repetitive. Luckily, we can factor out set-up code by implementing a
method called `setUp()`, which the testing framework will automatically call for every single test we run:

If the setUp() method raises an exception while the test is running, the framework will consider the test to have
suffered an error, and the test method will not be executed.

Similarly, we can provide a tearDown() method that tidies up after the test method has been run.

If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

Such a working environment for the testing code is called a **test fixture**. A new TestCase instance is created as a
unique test fixture used to execute each individual test method. Thus, `setUp(), tearDown(), and __init__()` will be
called once per test.

It is recommended that you use TestCase implementations to group tests together according to the features they test.
unittest provides a mechanism for this: the test suite, represented by unittest’s `TestSuite` class. In most cases,
calling unittest.main() will do the right thing and collect all the module’s test cases for you and execute them.

However, should you want to customize the building of your test suite, you can do it yourself.

### Skipping tests and expected failures

Unittest supports skipping individual test methods and even whole classes of tests. In addition, it supports marking a
test as an “expected failure,” a test that is broken and will fail, but shouldn’t be counted as a failure on a
TestResult.

Skipping a test is simply a matter of using the skip() decorator or one of its conditional variants, calling
TestCase.skipTest() within a setUp() or test method, or raising SkipTest directly.

