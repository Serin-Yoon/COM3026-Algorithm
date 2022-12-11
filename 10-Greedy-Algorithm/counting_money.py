money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = [0] * 8

value = int(input("- 거스름돈을 입력하세요: "))

for i in range(len(money)):
    cnt[i] = value // money[i]
    value = value % money[i]

for i in range(len(cnt)):
    print("- %d원 %d개" % (money[i], cnt[i]))