import heapq

for t in range(int(input())) : 
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m) :
        u, v, c= map(int, input().split())
        graph[u].append([v,c])
        
#         정점 방문 여부를 저장하는 리스트 정의
    visited = [False] * n
#     0번 정점에서 부터의 거리를 저장하는 리스트 정의
    dist = [-1] * n
#     우선순위 큐를 사용하기 위한 리스트 초기화 및 0번 정점 정보 heappush
    hq = []
    heapq.heappush(hq, (0,0))
    while len(hq) > 0 :
        d, u = heapq.heappop(hq)
        if visited[u] == False :#현재 정점이 방문되지 않았다면 진행 
            visited[u] = True
            dist[u]=d
            for i in range(len(graph[u])) :
                heapq.heappush(hq, (dist[u] + graph[u][i][1], graph[u][i][0]))
    print(dist[-1])