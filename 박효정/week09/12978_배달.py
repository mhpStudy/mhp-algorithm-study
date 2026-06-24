# 문제: 배달
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12978

'''
import heapq

def solution(N, road, K):
    
    # 다익스트라
    # 1. 시작점의 거리를 0으로 둔다
    # 2. 아직 처리하지 않은 노드 중 현재 거리가 가장 짧은 노드를 고른다.
    # 3. 그 노드를 거쳐 주변 노드로 가는 비용을 계산한다.
    # 4. 더 짧아지면 거리 값을 갱신한다.
    # 5. 반복
    
    # 1. 그래프 만들기
    # N 마을개수, road 도로정보, K 배달가능시간 
    graph = [[] for _ in range(N+1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 2. 최단거리 배열
    INF = float('inf')
    distance = [INF] * (N+1)
    distance[1] = 0 # 시작점에(1)에서 1번까지 가는 최단거리 0
    
    # 3. 우선순위 큐
    # (현재까지 걸린 시간, 현재 마을)
    heap = []
    heapq.heappush(heap, (0,1))
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        
        if dist > distance[node]:
            continue
        
        # 현재 마을과 연결된 마을 확인
        for next_node, cost in graph[node]:
            new_dist = dist + cost
            
            # 더 짧은 경로를 찾으면 갱신
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    
    # 4. K 이하 시간으로 배달 가능한 마을 수
    answer = 0
    for d in distance[1:]:
        if d <= K:
            answer += 1
    
    return answer
'''

def solution(N, road, K):
    INF = float('inf')

    # 거리 테이블 초기화
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    # 자기 자신까지의 거리는 0
    for i in range(1, N + 1):
        dist[i][i] = 0

    # 도로 정보 반영
    for a, b, cost in road:
        # 같은 두 마을 사이에 여러 도로가 있을 수 있으므로 더 짧은 도로만 저장
        dist[a][b] = min(dist[a][b], cost)
        dist[b][a] = min(dist[b][a], cost)

    # 플로이드 워셜
    for k in range(1, N + 1):          # 거쳐가는 마을
        for i in range(1, N + 1):      # 출발 마을
            for j in range(1, N + 1):  # 도착 마을
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 1번 마을에서 K 이하로 갈 수 있는 마을 개수
    answer = 0
    for i in range(1, N + 1):
        if dist[1][i] <= K:
            answer += 1

    return answer