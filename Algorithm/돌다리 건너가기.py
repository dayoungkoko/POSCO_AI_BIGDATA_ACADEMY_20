for _ in range(int(input())) : 
    n = int(input())
    cnt = [1,2,4]
    for i in range(3, n) :
        cnt.append((cnt[i-1]+cnt[i-2]+cnt[i-3])%1904101441)
    print(cnt[n-1])