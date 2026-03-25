import unittest


def valid_braces(string: str):
    last_elements = []
    for e in string:
        if (e == "(") or (e == "[") or (e == "{"):
            last_elements.append(e)
        else:
            if not last_elements:
                return False
            if (
                (e == ")" and last_elements[-1] != "(")
                or (e == "}" and last_elements[-1] != "{")
                or (e == "]" and last_elements[-1] != "[")
            ):
                return False
            else:
                last_elements.pop()
    return not last_elements


class Test(unittest.TestCase):

    def assert_valid(self, string):
        self.assertEqual(
            valid_braces(string), True, 'Expected "{0}" to be valid'.format(string)
        )

    def assert_invalid(self, string):
        self.assertEqual(
            valid_braces(string), False, 'Expected "{0}" to be invalid'.format(string)
        )

    def test(self):
        self.assert_valid("()")
        self.assert_invalid("(}")
        self.assert_valid("[]")
        self.assert_invalid("[(])")
        self.assert_valid("{}")
        self.assert_valid("{}()[]")
        self.assert_valid("([{}])")
        self.assert_invalid("([}{])")
        self.assert_valid("{}({})[]")
        self.assert_valid("(({{[[]]}}))")
        self.assert_invalid("(((({{")
        self.assert_invalid(")(}{][")
        self.assert_invalid("())({}}{()][][")


unittest.main()
