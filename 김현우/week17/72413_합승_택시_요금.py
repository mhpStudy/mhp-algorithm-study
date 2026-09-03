# 문제: 합승 택시 요금
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq


def solution(n, s, a, b, fares):
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))  # 양방향

    def dijkstra(start):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        pq = [(0, start)]  # (비용, 노드) 순서

        while pq:
            dist, node = heapq.heappop(pq)

            if dist > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                next_dist = dist + weight
                if next_dist < distances[neighbor]:
                    distances[neighbor] = next_dist
                    heapq.heappush(pq, (next_dist, neighbor))
        return distances

    # 3. 각 지점(S, A, B)에서 출발하는 최단 거리
    dist_from_s = dijkstra(s)
    dist_from_a = dijkstra(a)
    dist_from_b = dijkstra(b)

    min_cost = float('inf')
    for i in range(1, n + 1):
        # S->X (합승) + X->A (무지 따로) + X->B (어피치 따로)
        cost = dist_from_s[i] + dist_from_a[i] + dist_from_b[i]
        if cost < min_cost:
            min_cost = cost

    return min_cost

