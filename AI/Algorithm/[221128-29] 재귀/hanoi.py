import sys
sys.setrecursionlimit(1000000)

def hanoi(start, mid, end, n) :
    if n== 0 :
        return 0
    else:
        hanoi(start, end, mid, n-1)
        print(start,'->',end)
        hanoi(mid, start, end, n-1)

t=int(input())
for _ in range(t) :
    n=int(input())
    hanoi('A','B','C',n)