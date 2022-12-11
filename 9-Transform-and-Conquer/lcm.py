def gcd(n, m):
    r = n % m
    if r == 0:
        return m
    else:
        return gcd(m, r)

def lcm(n, m):
    return n * m // gcd(n, m)

print(lcm(1071, 1029))