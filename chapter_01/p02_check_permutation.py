import time
import unittest
from collections import defaultdict, Counter

def is_permutation(string, permutation):
    return sorted(string) == sorted(permutation)


def is_permutation2(string, permutation):
    dict_1 = {}
    dict_2 = {}
    
    for letter in string:
        dict_1[letter] = dict_1.get(letter, 0) + 1
    for letter in permutation:
        dict_2[letter] = dict_2.get(letter, 0) + 1
    
    return dict_1 == dict_2


def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True


def check_permutation_pythonic(str1, str2):
    # short-circuit to avoid instantiating a Counter which for big strings
    # may be an expensive operation
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        is_permutation,
        is_permutation2,
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_cp(self):
        num_runs = 10000
        function_runtimes = defaultdict(float)

        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                start = time.perf_counter()
                assert check_permutation(str1, str2) == expected
                function_runtimes[check_permutation.__name__] += (
                        time.perf_counter() - start
                    ) * 1000
            
        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
