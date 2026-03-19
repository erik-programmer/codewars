import unittest


# [20, 37, 20, 20, 21], 2 = [20, 37, 20, 21]
def delete_nth(order, max_e):
    d = {}
    r = []
    for e in order:
        d[e] = d.get(e, 0) + 1
        if d[e] <= max_e:
            r.append(e)
    return r


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(
            delete_nth([20, 37, 20, 21], 1),
            [20, 37, 21],
            "From list [20, 37, 20, 21], 1 you get",
        )
        self.assertEqual(
            delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
            [1, 1, 3, 3, 7, 2, 2, 2],
            "From list [1, 1, 3, 3, 7, 2, 2, 2, 2], 3 you get",
        )
        self.assertEqual(
            delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3),
            [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5],
            "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3 you get",
        )
        self.assertEqual(
            delete_nth([1, 1, 1, 1, 1], 5),
            [1, 1, 1, 1, 1],
            "From list [1, 1, 1, 1, 1], 5 you get",
        )
        self.assertEqual(delete_nth([], 5), [], "From list [], 5 you get")
        self.assertEqual(
            delete_nth([12, 39, 19, 39, 39, 19, 12], 1),
            [12, 39, 19],
            "From list [12, 39, 19, 39, 39, 19, 12], 1 you get",
        )


unittest.main()
