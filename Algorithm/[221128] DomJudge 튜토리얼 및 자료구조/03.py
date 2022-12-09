t=int(input())
for i in range(t) :
    result=0
    lst=list(input().split())
    for i in lst :
        result+=int(i)
    print(result)