import unittest


def find_missing_letter(chars):
    for i, _ in enumerate(chars):
        if ord(chars[i]) + 1 != ord(chars[i + 1]):
            return chr(ord(chars[i + 1]) - 1)


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(find_missing_letter(["a", "b", "c", "d", "f"]), "e")
        self.assertEqual(find_missing_letter(["O", "Q", "R", "S"]), "P")
        self.assertEqual(find_missing_letter(["b", "d"]), "c")


unittest.main()
