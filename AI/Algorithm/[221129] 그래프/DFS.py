import sys
sys.setrecursionlimit(1000000)

def DFS(v, list, Check) : #v에서 DFS 시작
    print(v, end=' ')
    check[v]= True
    for i in list[v] :
        if check[i] == False :
            DFS(i, list, Check)

t=int(input())
for _ in range(t) :
    n, m=map(int ,input().split())
    list=[[] for _ in range(n)]
    for i in range(m) :
        u, v=map(int, input().split())
        list[u].append(v)
        list[v].append(u)
    for i in range(n) :
        list[i].sort()
    
    check = [False] * n
    DFS(0,list, check)
    print(" ")