# 시작은 언제나 1번 마을, K시간 이하로 배달이 가능한 마을만 세기

'''
dijkstra(다익스트라)
[성능 요약] 메모리: 12.2 MB 시간: 0.50 ms 
'''
import heapq
def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]

    # 양방향
    for u,v,w in road:
        graph[u].append((w,v))
        graph[v].append((w,u))

    INF = 50*10000 + 1
    pq = [(0,1)]
    dist = [INF] * (N+1)
    dist[1] = 0

    while pq:
        w,n = heapq.heappop(pq)
        
        # 이전에 더 적은 경로로 온적이 있다면 pass
        if dist[n] < w :
            continue
        
        for next_w, next_n in graph[n]:
            new_w = w + next_w

            # 배달 갈 수 없으면 쳐내기
            if new_w > K:
                continue
            
            # 이전에 더 적은 경로로 온적이 있다면 pass
            if dist[next_n] < new_w:
                continue
            
            dist[next_n] = new_w
            heapq.heappush(pq,(new_w, next_n))
        
    for d in dist:
        if d <= K:
            answer +=1

    return answer


'''
플로이드 워셜
거쳐가는 노드 기준으로 돌면서 해당 노드를 거쳐가는 경로를 확인하며 최단 거리 갱신
a -> b -> c 의 관계가 있다면 (a->b + b->c) 와 (a->c) 경로 중 최단을 선택
[성능 요약] 메모리: 11.7 MB 시간: 11.46 ms
'''
 
def solution(N, road, K):
    answer = 0

    INF = 50*10000 + 1
    matrix = [[INF] * (N+1) for _ in range(N+1)]

    # 예시 보니까 3->5 , 5->3 처럼 가중치가 다른 경우가 있어서 꼭 최소값인지 체크해줘야함
    for u,v,w in road:
        matrix[u][v] = min(w, matrix[u][v])
        matrix[v][u] = min(w, matrix[u][v])

    for i in range(N+1):
        matrix[i][i] = 0


    #  k:경유지, i:출발지, j:도착지
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

    # 출력 확인용
    # for i in range(N+1):
    #     for j in range(N+1):
    #         print(matrix[i][j],end=" ")
    #     print()

    for j in range(1,N+1):
        if matrix[1][j] <= K:
            answer += 1

    return answer


print(solution(	5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))