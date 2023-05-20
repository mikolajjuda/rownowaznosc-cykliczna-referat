def rownowazne_cyklicznie(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    n = len(a)
    for c in range(n):
        for k in range(n):
            if a[(c + k) % n] != b[k]:
                break
        else:
            return True
    return False
