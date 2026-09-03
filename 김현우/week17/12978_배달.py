# 문제: 배달
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq


def solution(N, road, K):

    cost = [K + 1 for _ in range(N + 1)]  # 각 마을까지 걸리는 시간을 저장. 최대로 초기화
    cost[1] = 0

    # heapq는 첫 번째 원소 기준으로 정렬하므로 [시간, 마을] 순서
    pq = [[0, 1]]  # [시간, 마을]

    while pq:
        t, n = heapq.heappop(pq)
        if t > cost[n]: continue

        # 현재 마을에서 연결된 모든 마을을 찾자
        for town1, town2, time in road:

            # Case 1: 출발지가 town1인 경우
            if town1 == n:
                if cost[town2] > cost[town1] + time:
                    cost[town2] = cost[town1] + time
                    heapq.heappush(pq, [cost[town2], town2])

                    # Case 2: 출발지가 town2인 경우
            elif town2 == n:
                if cost[town1] > cost[town2] + time:
                    cost[town1] = cost[town2] + time
                    heapq.heappush(pq, [cost[town1], town1])

    return sum(1 for c in cost if c <= K)



def solution2(N, road, K):
    # 1. 인접 리스트 생성 (현재 마을과 연결된 도로만 바로 찾기 위함)
    graph = [[] for _ in range(N + 1)]
    for town1, town2, time in road:
        graph[town1].append((town2, time))
        graph[town2].append((town1, time))  # 양방향 도로 처리

    # 2. 최단 거리 배열 초기화 (K+1보다 안전하게 무한대 'inf' 사용)
    cost = [float('inf')] * (N + 1)
    cost[1] = 0

    # 3. 우선순위 큐 초기화 (정렬 기준이 되는 '시간'을 앞에 배치: [시간, 마을])
    pq = [[0, 1]]

    while pq:
        t, n = heapq.heappop(pq)

        # 이미 방문해서 더 짧은 거리가 확정된 마을이라면 무시
        if t > cost[n]:
            continue

        # 💡 핵심: 현재 마을(n)과 연결된 도로만 쏙 골라서 확인! (road 전체 안 봄)
        for next_town, time in graph[n]:
            next_cost = t + time  # 현재까지 걸린 시간 + 다음 도로 시간

            if next_cost < cost[next_town]:
                cost[next_town] = next_cost
                heapq.heappush(pq, [next_cost, next_town])

    # 4. K 시간 이하로 걸리는 마을의 개수 세기
    return sum(1 for c in cost if c <= K)
