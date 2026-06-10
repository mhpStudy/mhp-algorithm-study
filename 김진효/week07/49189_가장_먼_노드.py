 # [성능 요약] 메모리: 29.6 MB 시간: 49.68 ms 

#  최단경로 dijkstra -> 한 정점에서 다른 정점의 최단 거리를 구할 때 쓰임
import heapq

def solution(n, edge):
    answer = 0

    # 양방향 그래프
    graph = [[] for _ in range(n+1)]
    for u,v in edge:
        graph[u].append([1, v])
        graph[v].append([1, u])

    
    # 1번 노드에서부터 각 노드까지 최단 경로 찾기
    max_w = 0
    pq = [(0, 1)]
    dist = [20001] * (n+1)
    dist[0] = 0
    dist[1] = 0


    while pq:
        w, node = heapq.heappop(pq)

        #  이전에 더 적은 경로로 온 경우가 있는 경우
        if dist[node] < w:
            return
        
        for next_w, next_n in graph[node]:

            
            # 다음 노드로 가기 위한 가중치
            new_w = next_w + w


            # 새로운 가중치가 더 큰 경우 return
            if new_w >= dist[next_n]:
                continue
            
            # 가장 멀리 떨어져 있는지 판별하여 갱신
            max_w = max(new_w,max_w)

            dist[next_n] = new_w
            heapq.heappush(pq,(new_w,next_n))

    # 가장 멀리 떨어진 노드 수 세기
    answer = dist.count(max_w)

    return answer