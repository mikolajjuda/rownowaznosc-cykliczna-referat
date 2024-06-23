from naive import rownowazne_cyklicznie as naive
from pattern_matching import rownowazne_cyklicznie as pattern_matching
from fast import rownowazne_cyklicznie as fast


def run_test(test):
    a = list(map(int, test[0].split())) if " " in test[0] else list(test[0])
    b = list(map(int, test[1].split())) if " " in test[1] else list(test[1])
    answer = test[2] == "TAK"

    if naive(a, b) != answer:
        print("naive wrong")
        exit(1)
    if pattern_matching(a, b) != answer:
        print("pattern_matching wrong")
        exit(1)
    if fast(a, b) != answer:
        print("fast wrong")
        exit(1)


with open("testy.txt") as f:
    lines = f.read().splitlines()
    tests = []
    for i in range(0, len(lines), 3):
        tests.append(lines[i : i + 3])
    for test in tests:
        run_test(test)
    print("OK")
