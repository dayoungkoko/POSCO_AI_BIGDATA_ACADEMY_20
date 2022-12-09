t=int(input())
for _ in range(t) :
    num = int(input())
    FIB = [1,1]
    for i in range(2, num) :
        FIB.append(FIB[i-1] + FIB[i-2])
    print(FIB[num-1])