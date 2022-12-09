t=int(input())
for _ in range(t) :  
    n, m = list(map(int,input().split()))
    lst=[[]*n for _ in range(n)]
    for _ in range(m) :
        u, v= list(map(int,input().split()))
        lst[u].append(v)
        lst[v].append(u)
        
        lst[u].sort()
        lst[v].sort()
    for _ in range(n) :
        print(*lst[_])