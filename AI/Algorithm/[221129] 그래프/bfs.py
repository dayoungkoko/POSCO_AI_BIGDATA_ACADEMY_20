from collections import deque
t=int(input())
for _ in range(t) :
    n, m = list(map(int,input().split()))
    lst=[[]*n for _ in range(n)]
    result=[]
    q=deque([])
    for _ in range(m) :
        u, v= list(map(int,input().split()))
        lst[u].append(v)
    for i in range(n) :
        lst[i].sort()
    q.append(0)
    while q!=deque([]) :
        node = q.popleft()
        if node not in result :
            result.append(node)
        for i in lst[node] :
            if i in result :
                pass
            else :
                q.append(i)
    print(*result)