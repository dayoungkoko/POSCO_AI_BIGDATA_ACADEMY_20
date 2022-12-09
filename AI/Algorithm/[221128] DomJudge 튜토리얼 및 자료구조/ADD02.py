from collections import deque

t=int(input())
for _ in range(t) :
    car=list(input().split())
    queue = deque([])
    for c in car :
        if c not in queue : 
            queue.append(c)
        else :
            queue.popleft()
    if queue!=deque([]) :
        print('YES')
    else :
        print('NO')