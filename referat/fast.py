def rownowazne_cyklicznie(A: list, B: list) ->bool:
    if len(A) != len(B):
        return False
    n = len(A)
    i = -1
    j = -1
    while i<n-1 and j<n-1:
        for k in range(1, n+1):
            if A[(i+k)%n] != B[(j+k)%n]:
                if A[(i+k)%n] < B[(j+k)%n]:
                    j += k+1
                else:
                    i += k+1
                break
        else:
            return True
    return False
