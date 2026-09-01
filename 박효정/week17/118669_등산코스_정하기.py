# 문제: 등산코스 정하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/118669
 # [성능 요약] 메모리: 88.4 MB 시간: 4541.55 ms  // summits을 그대로 썼을 때 
 # [성능 요약] 메모리: 89 MB 시간: 264.12 ms  // summits 을 set으로 바꿨을 때 

'''
1. 출입구 - 노드 - 봉우리 - 노드 - 출입구 
2. 처음 시작한 출입구 외 다른 출입구로 나오면 안 됨
3. intensity는 단일 간선의 가중치

[로직1 - 시간초과로 실패]
- dijkstra를 함수로 빼고 출입구와 봉우리마다 for문으로 돌린다
- 출입구-봉우리, 봉우리-출입구 경로에서 각각 최대 가중치를 구하고, min으로 최종 값을 뽑은 다음 list에 튜플 (instensity, 봉우리) 순으로 담는다
- list를 정렬해 가장 앞 원소를 1, 0 인덱스 순서로 answer에 담는다

[로직2]
- 어느 출입구에서 시작하든 상관없이 특정 봉우리까지 도달하는 최적값을 구한다
- 어차피 그대로 밟아 내려오면 되므로 왕복경로를 계산할 필요 없다
- 모든 gates를 heap에 넣고 시작해, 봉우리의 dist 값을 찾는다

'''
import heapq

def dijkstra(n, graph, gates, summits):
    INF = float('inf')
    dist = [INF] * (n+1)
    heap = []
    summits_set = set(summits)
    
    # 모든 시작지점을 표시하고 heap에 넣는다
    for g in gates:
        dist[g] = 0
        heapq.heappush(heap, (0, g))
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        # 봉우리일 경우 지나가지 않음
        # 다른 출입구(g2)는 왜 안막지?
        # dist[g2]가 0이기 때문에 new_dist < dist[g2]가 성립 불가능.. 경로에 영향을 주지 못함
        if cur_node in summits_set:
            continue
        
        # 지금 꺼낸 값이 지금까지의 최선값보다 크면 낡은 정보니까 무시
        # 같은 노드가 여러 값으로 중복되어 들어갔을 때를 대비
        if cur_dist > dist[cur_node]:
            continue
        
        for neighbor, weight in graph[cur_node]:
            # cur_dist: 시작점에서 cur_node까지 오는 동안 거친 구간 중 가장 길었던 시간
            # weight: cur_node에서 neighbor까지 가는 이번 구간의 시간
            # intensity: 전체 경로에서 가장 긴 시간이므로 max로 계산
            new_dist = max(cur_dist, weight)
            
            # 새 intensity가 기존 경로보다 최적인 경우에만 갱신
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
                
    return dist

def solution(n, paths, gates, summits):
    li = []
    
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    
    di = dijkstra(n, graph, gates, summits)
    for s in summits:
        li.append((di[s], s))

    li.sort()
    answer = [li[0][1], li[0][0]]
    
    return answer