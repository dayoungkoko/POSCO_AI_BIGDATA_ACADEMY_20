import heapq
t=int(input())
for i in range(t) :
    lst_in = list(input().split())
    hq=[]
    for i in lst_in :
        if int(i)>0 :
            heapq.heappush(hq,int(i))
        elif int(i)==-1 :
            print(heapq.heappop(hq), end=' ')
    print()