import unittest
import testlib
import xmlrunner

class TestMapping(unittest.TestCase):

    def test_comparing(self):
        result = testlib.image_compare(1)
        self.assertEqual(result, True)


if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
