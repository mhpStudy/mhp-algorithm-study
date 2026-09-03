# 문제: 등산코스 정하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/118669

import heapq


def solution(n, paths, gates, summits):
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    summit_set = set(summits)

    # 3. 다중 출발
    pq = []
    intensity_table = [float('inf')] * (n + 1)

    for gate in gates:
        intensity_table[gate] = 0
        heapq.heappush(pq, (0, gate))  # (intensity, 노드)

    while pq:
        intensity, node = heapq.heappop(pq)

        # 이미 더 좋은(작은) 인텐시티로 방문했다면 패스
        if intensity > intensity_table[node]:
            continue

        # 산봉우리에 도착했다면 정지
        if node in summit_set:
            continue

        for neighbor, weight in graph[node]:
            # 다음 노드로 갈 때의 인텐시티 = max(지금까지 중 최대, 이번 간선)
            next_intensity = max(intensity, weight)

            if next_intensity < intensity_table[neighbor]:
                intensity_table[neighbor] = next_intensity
                heapq.heappush(pq, (next_intensity, neighbor))

    # 문제 요구사항 맞추기: 인텐시티가 가장 작은 산봉우리 찾기
    # 산봉우리 번호가 작은 것을 출력해야 하므로 정렬
    summits.sort()
    result_summit = 0
    min_intensity = float('inf')

    for summit in summits:
        if intensity_table[summit] < min_intensity:
            min_intensity = intensity_table[summit]
            result_summit = summit

    return [result_summit, min_intensity]
