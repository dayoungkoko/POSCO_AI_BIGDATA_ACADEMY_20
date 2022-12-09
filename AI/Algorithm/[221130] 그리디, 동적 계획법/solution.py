t=int(input())
for _ in range(t) :
    N, C=map(int, input().split())
    liquidlist=[]
    for i in range(N) :
        w,v=map(int, input().split())
        liquidlist.append((w/v, w, v))
    liquidlist.sort(reverse = True)
    maxg = 0
    for i in range(N) :
        if C>=liquidlist[i][2] :
            maxg +=liquidlist[i][1]
            C-=liquidlist[i][2]
        else :
            maxg += C*(liquidlist[i][0])
            break
    print(int(maxg))