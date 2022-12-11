def lcs(a, b):
    LCS = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    return LCS[-1][-1]

def compare(s0, s1, s2):
    r1 = lcs(s0, s1)
    r2 = lcs(s0, s2)

    if (r1 > r2):
        print("유사 단어:", s1)
    elif (r1 < r2):
        print("유사 단어:", s2)
    else:
        print("두 단어 모두 유사")

compare("topato", "tophat", "tomato")