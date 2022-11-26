import time

def rpm(a, b, add):
    if a == 1:
        return b + add
    elif a % 2 == 0:
        return rpm(a//2, b*2, add)
    else:
        return rpm(a//2, b*2, add+b)

def rpm2(a, b, add):
    while a > 1:
        if a % 2 != 0:
            add += b
        a = a // 2
        b = a * 2
    return b + add

a = 195342362382473513845003428
b = 399253634579252174384

start1 = time.time()
print("Russian Peasant X:", a * b, end=" ")
print("%.7f seconds" % (time.time() - start1))

start2 = time.time()
res = rpm(a, b, 0)
print("Russian Peasant 1:", res, end=" ")
print("%.7f seconds" % (time.time() - start2))

start3 = time.time()
res2 = rpm(a, b, 0)
print("Russian Peasant 2:", res2, end=" ")
print("%.7f seconds" % (time.time() - start3))
