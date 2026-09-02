'''
[성능 요약] 메모리: 16.9 MB 시간: 29.16 ms 
[채점 결과] 정확성: 50.0, 효율성: 50.0, 합계: 100.0 / 100.0
'''

# 시작점에서 각 정점까지 가보고, 그 정점에서 A와 B를 가보기
# n(지점의 개수), s(출발), a(A의 도착), b(B의 도착), fares(예상 택시요금)

import heapq

def solution(n, s, a, b, fares):
    answer = 0

    def dijkstra(start, n, init):
        pq = [(0,start)]        # (누적거리, 노드번호)
        dists = [init] * (n+1)  # 각 노드까지의 최단거리를 정할 리스트
        dists[start] = 0

        while pq:
            dist, node = heapq.heappop(pq)

            # 이전보다 더 적은 경로로 온 적이 있는 경우 진행 x
            if dists[node] < dist:
                continue

            # 경로 탐색
            for next_d, next_n in g[node]:
                # 다음 정점까지 걸릴 거리 계산
                new_dist = dist + next_d

                # 이전보다 더 적은 경로로 온 적이 있는 경우 진행 x
                if dists[next_n] < new_dist:
                    continue

                heapq.heappush(pq,(new_dist,next_n))
                dists[next_n] = new_dist

        return dists

    # 경로 최대값
    init = 100000 * (n-1) + 1

    # 간선 정보 저장
    g = [[] for _ in range(n+1)]
    for u,v,w in fares:
        g[u].append((w,v))
        g[v].append((w,u))

    # 최단 경로 탐색
    s_dist = dijkstra(s,n,init)
    a_dist = dijkstra(a,n,init)
    b_dist = dijkstra(b,n,init)

    # 최저 택시요금 계산해보기 (시작 정점에서 따로 갈지, 합승해서 갈지)
    answer = s_dist[a] + s_dist[b]
    for i in range(1,n+1):
        if i == s:
            continue
        answer = min(answer, s_dist[i] + a_dist[i] + b_dist[i])

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))