import collections
t=int(input())
for i in range(t) :
    queue=collections.deque([])
    lst_in = list(map(int,input().split()))
    for i in lst_in :
        if i > 0 :
            queue.append(i)
        elif i == -1 :
            print(queue.popleft(), end=' ')