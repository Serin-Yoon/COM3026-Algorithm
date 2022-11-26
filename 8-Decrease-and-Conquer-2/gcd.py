def gcd(n, m):
    r = n % m
    if r == 0:
        return m
    else:
        return gcd(m, r)

print(gcd(1071, 1029))