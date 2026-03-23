import unittest


def solution(s: str):
    return s[:1] + "".join(e if e.islower() else f" {e}" for e in s[1:])


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(solution(""), "")


unittest.main()
