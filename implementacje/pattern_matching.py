def rownowazne_cyklicznie(A: list, B: list) -> bool:
    if len(A) != len(B):
        return False
    n = len(A)

    pmt = [0] * n
    for i in range(1, n):
        k = pmt[i - 1]
        while k > 0 and B[i] != B[k]:
            k = pmt[k - 1]
        if B[i] == B[k]:
            k += 1
        pmt[i] = k
    
    j=0
    for i in range(2*n):
        while j>0 and A[i%n] != B[j]:
            j = pmt[j-1]
        if A[i%n] == B[j]:
            if j == n-1:
                return True
            j += 1

    return False
