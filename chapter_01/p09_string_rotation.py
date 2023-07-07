# O(N)
import unittest


def is_rotated_string(s1, s2):
    """Checks if s2 is a rotation of s1"""
    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return True
    return False


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1, s2)
            assert actual == expected
            actual = is_rotated_string(s1, s2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
