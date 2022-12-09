t=int(input())
lst=[]
for i in range(t) :
    lst_in=list(input().split())
    for i in lst_in : 
        if int(i)>0 :
            lst.append(int(i))
        elif int(i)==-1 :
            print(lst.pop(), end=' ')