import unittest


# print(max(players, key=lambda p: p.price))
# high('man i need a taxi up to ubud'), 'taxi'
def high(x: str):
    return max(x.split(" "), key=lambda w: sum(ord(l) - 96 for l in w))


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(high("man i need a taxi up to ubud"), "taxi")
        self.assertEqual(high("what time are we climbing up the volcano"), "volcano")
        self.assertEqual(high("take me to semynak"), "semynak")
        self.assertEqual(high("aa b"), "aa")
        self.assertEqual(high("b aa"), "b")
        self.assertEqual(high("bb d"), "bb")
        self.assertEqual(high("d bb"), "d")
        self.assertEqual(high("aaa b"), "aaa")


unittest.main()
