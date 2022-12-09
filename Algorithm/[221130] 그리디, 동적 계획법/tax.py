for _ in range(int(input())):
    tax = int(input())
    num = 0
    while tax > 0:
        if tax // 50000 > 0:
            num += tax // 50000
            tax -= 50000 * (tax // 50000)
        elif tax // 10000 > 0:
            num += tax // 10000
            tax -= 10000 * (tax // 10000)
        elif tax // 5000 > 0:
            num += tax // 5000
            tax -= 5000 * (tax // 5000)
        elif tax // 1000 > 0:
            num += tax // 1000
            tax -= 1000 * (tax // 1000)
        elif tax // 500 > 0:
            num += tax // 500
            tax -= 500 * (tax // 500)
        else:
            num += tax // 100
            tax = 0
    print(num)