# 문제: 배달
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12978
# [성능 요약] 메모리: 11.9 MB 시간: 0.77 ms 

import heapq

# 마을의 개수 N, 도로 정보 road, 배달 가능 시간 K
# 음식 주문을 받을 수 있는 마을의 개수 return 
# 시작점은 항상 1. 1로부터 각 마을까지의 최단거리를 계산해서 K이하면 answer에 추가.
# road = [[1, 2, 1]] 연결된 마을 a, b , 가중치 c 
def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)] # 0은 안 쓸 것
    
    for a, b, c in road:
        graph[a].append((b, c)) # 이웃, 가중치 순
        graph[b].append((a, c)) # 양방향
    
    INF = float('inf')
    dist = [INF] * (N+1)
    
    heap = []
    # 시작지점
    heapq.heappush(heap, (0, 1)) 
    dist[1] = 0
    
    while heap:
        # 1. 현재노드 뽑기
        cur_dist, cur_node = heapq.heappop(heap)
        
        # 2. 기존 최단거리보다 크다면 또 보지 않음
        if cur_dist > dist[cur_node]:
            continue
        
        # 3. 이웃한 노드들 확인
        for neighbor, weight in graph[cur_node]:
            # 새로 갱신될 거리
            new_dist = cur_dist + weight
            # 기존 최단거리보다 작다면 갱신하고 heap에 넣음
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    # dist돌면서 각 마을까지 걸리는 시간 확인
    for t in dist:
        if t <= K:
            answer += 1
        
    return answer
