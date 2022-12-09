import sys
sys.setrecursionlimit(1000000)

def FIB1(n) :
    if n==1 or n==2 :
        return 1
    else :
        return FIB1(n-1) + FIB1(n-2)
    
t=int(input())
for _ in range(t) :
    n=int(input())
    result = FIB1(n)
    print(result)