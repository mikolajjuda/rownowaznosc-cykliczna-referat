def rownowazne_cyklicznie(A: list, B: list) -> bool:
    if len(A) != len(B):
        return False
    n = len(A)
    
    for l in range(n):
        for k in range(n):
            if A[(l + k) % n] != B[k]:
                break
        else:
            return True
    return False
