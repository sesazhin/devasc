import unittest


# class MyTestCase(unittest.TestCase):

def compare_numbers(num1, num2):
    return num1 == num2

'''
def divide_numbers(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return 0.0
'''


def divide_numbers(num1, num2):
    return num1/num2


class TestSumKV2(unittest.TestCase):
    '''
    def __init__(self):
        super().__init__()

        self.a = 5
        self.b = 5
    '''

    def __init__(self, *args, **kwargs):
        # super(TestSumKV2, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.a = 0
        self.b = 0

    def setUp(self):
        print('Starting the test')

    def test1(self):

        if not self.a or not self.b:
            self.skipTest("self.a or self.b are equal to 0!")

        self.assertEqual(self.a, self.b)



    '''
    def test3(self):
        self.assertFalse(compare_numbers(self.a, self.b), "Numbers are equal")
    '''

    def test4(self):
        num1 = 4
        num2 = 0
        # tst = lambda num1, num2: num1 / num2
        # self.assertRaises(ZeroDivisionError, lambda: num1/num2)
        # self.assertRaises(ZeroDivisionError, lambda: divide_numbers(num1, num2))
        # self.assertRaises(ZeroDivisionError, divide_numbers, num1, num2)

        with self.assertRaises(ZeroDivisionError):
            print('This test begins')
            divide_numbers(num1, num2)
            print('This test failed - exception not raised')

    def test5(self):
        self.assertTrue(compare_numbers(self.a, self.b), "Numbers aren't equal")
        # self.assertEqual(2, 3)

class TestSumKV(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, 2)

    def test2(self):
        self.assertEqual(33, 33)


if __name__ == '__main__':
    unittest.main()