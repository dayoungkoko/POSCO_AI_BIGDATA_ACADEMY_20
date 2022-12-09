t=int(input())
for _ in range(t) :  
    n, m = list(map(int,input().split()))
    matrix = [[0]*n for _ in range(n)]
    for _ in range(m) :
        u, v, c= list(map(int,input().split()))
        matrix[u][v]=c
    for _ in range(n) :
        print(*matrix[_])