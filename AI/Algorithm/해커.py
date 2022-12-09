t = int(input())
for _ in range(t) :
    N,M = map(int, input().split())
    lst = [[] for _ in range(N)]
    for i in range(M) :
        u,v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)
    cnt = 0 
    check=[False]*N
    stk = [0]
    while True : 
        cnt += 1
        while stk :
            v = stk.pop()
            if check[v] == True :
                continue
            check[v] = True
            for i in lst[v] :
                if check[i] == False :
                    stk.append(i)
        if check.count(True) == N:
            break
        else : 
            stk.append(check.index(False))
    print(cnt)