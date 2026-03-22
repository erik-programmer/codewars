import unittest


def count_smileys(arr: list[str]):
    c = 0
    for i, e in enumerate(arr):
        if len(e) == 2:
            if (e[0] == ":" or e[0] == ";") and (e[1] == ")" or e[1] == "D"):
                c += 1
        elif len(e) == 3:
            if (
                (e[0] == ":" or e[0] == ";")
                and (e[1] == "-" or e[1] == "~")
                and (e[2] == ")" or e[2] == "D")
            ):
                c += 1
    return c


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(count_smileys([]), 0)
        self.assertEqual(count_smileys([":D", ":~)", ";~D", ":)"]), 4)
        self.assertEqual(count_smileys([":)", ":(", ":D", ":O", ":;"]), 2)
        self.assertEqual(count_smileys([";]", ":[", ";*", ":$", ";-D"]), 1)


unittest.main()
