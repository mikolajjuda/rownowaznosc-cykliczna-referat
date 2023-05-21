def rownowaznosc_cykliczna(A: list, B: list) -> bool:
    if len(A) != len(B):
        return False
    AA = A + A
    return KMPSearchExists(B, AA)


def KMPSearchExists(pattern, word) -> bool:
    M = len(pattern)
    N = len(word)
    lps = [0] * M
    j = 0
    computeLPSArray(pattern, M, lps)
    i = 0
    while i < N:
        if pattern[j] == word[i]:
            i += 1
            j += 1
        if j == M:
            return True
        elif i < N and pattern[j] != word[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def computeLPSArray(pat, M, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1
