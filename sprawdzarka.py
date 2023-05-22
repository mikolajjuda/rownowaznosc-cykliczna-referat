from implementacje.naive import rownowazne_cyklicznie as naive
from implementacje.pattern_matching import rownowazne_cyklicznie as pattern_matching
from implementacje.fast import rownowazne_cyklicznie as fast


def run_test(test):
    a = list(test[0])
    b = list(test[1])
    answer = True if test[2] == "TAK" else False

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
