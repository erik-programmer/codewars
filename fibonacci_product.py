import unittest


def product_fib(_prod):
    fib_1 = 0
    fib_2 = 1
    while fib_2 * fib_1 < _prod:
        fib_3 = fib_1
        fib_1 = fib_2
        fib_2 = fib_3 + fib_2
    if fib_2 * fib_1 == _prod:
        return [fib_1, fib_2, True]
    if fib_2 * fib_1 > _prod:
        return [fib_1, fib_2, False]


product_fib(124)


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(product_fib(0), [0, 1, True])
        self.assertEqual(product_fib(5895), [89, 144, False])


unittest.main()
