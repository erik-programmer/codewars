import unittest

# tower_builder(3), ["  *  ", " *** ", "*****"]


def tower_builder(n_floors):
    return list(
        " " * (n_floors - i - 1) + "*" * (i * 2 + 1) + " " * (n_floors - i - 1)
        for i in range(0, n_floors)
    )


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(
            tower_builder(1),
            [
                "*",
            ],
        )
        self.assertEqual(tower_builder(2), [" * ", "***"])
        self.assertEqual(tower_builder(3), ["  *  ", " *** ", "*****"])


unittest.main()
