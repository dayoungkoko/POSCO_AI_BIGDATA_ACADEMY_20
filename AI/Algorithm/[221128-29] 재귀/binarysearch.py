import sys
sys.setrecursionlimit(1000000)

def binary(data, left, right, q) : #data의 left - right 범위 내에서 q의 위치를 반환하는 함수
    # 종료조건 1. 리스트 크기 
    if left > right :
        return -1
    mid = (left+right)//2  # 중간 위치의 값 결정
    # 종료조건 2. 원하는 값 찾음
    if data[mid] == q :
        return mid
    # 문제 분할 : q와 data[mid]의 관계에 따라 부분문제를 호출
    if data[mid] > q :
        sub = binary(data, left, mid-1, q)
    elif data[mid] < q : 
        sub = binary(data, mid+1, right, q)
    return sub
    

t = int(input())
for _ in range(t) :
    ans=[]
    data=list(map(int,input().split()))
    query=list(map(int,input().split()))
    for q in query :
        ans.append(binary(data, 0, len(data)-1, q))
    print(*ans)