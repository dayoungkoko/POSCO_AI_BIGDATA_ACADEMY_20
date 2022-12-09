import sys
sys.setrecursionlimit(1000000)


def func(n, k, m):
    if k == 0:
        return 1
    elif k==1 :
        return n%m
    elif k % 2 == 0:
        return (func(n, k / 2, m) * func(n, k/2, m)) % m
    elif k % 2 != 0:
        return (func(n, k-1, m) * func(n,1,m))%m


t = int(input())
for _ in range(t):
    n, k, m = map(int, input().split())
    print(func(n, k, m))