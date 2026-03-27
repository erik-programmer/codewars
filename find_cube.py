import unittest


def find_nb(m):
    s = 0
    for i in range(1, m):
        s += i**3
        if s == m:
            return i
        if s > m:
            return -1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_nb(4), -1)
        self.assertEqual(find_nb(16), -1)
        self.assertEqual(find_nb(4183059834009), 2022)
        self.assertEqual(find_nb(24723578342962), -1)
        self.assertEqual(find_nb(135440716410000), 4824)
        self.assertEqual(find_nb(40539911473216), 3568)
        self.assertEqual(find_nb(26825883955641), 3218)


unittest.main()
