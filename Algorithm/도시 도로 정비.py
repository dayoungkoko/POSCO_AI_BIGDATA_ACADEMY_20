t=int(input())
for _ in range(t) :
    n =int(input())
    co= []
    tot = 0
    for _ in range(n) :
        co.append(list(map(int, input().split())))
    for i in range(0, n-1) :
        for j in range(i+1,n) :
            tot+=abs(co[i][0] - co[j][0])+abs(co[i][1] - co[j][1])
    print(tot)