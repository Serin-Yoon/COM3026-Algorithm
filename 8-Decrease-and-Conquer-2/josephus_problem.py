def josephus(m, n):
    ppl = [i for i in range(1, m + 1)]
    idx = 0
    while len(ppl) > 2:
        idx += (n - 1)
        if idx > len(ppl) - 1:
            idx -= len(ppl)
        del ppl[idx]
    del ppl[n % 2 - 1]
    return ppl[0]

print(josephus(40, 3))