import heapq

def solution(N, road, K):
    answer = 0

    # 양방향 그래프 저장(a:출발, b:도착, c:걸리는시간)
    g = [[] for _ in range(N+1)]

    for a,b,c in road:
        g[a].append((c,b))
        g[b].append((c,a))

    init = 50*10000
    pq = [(0,1)]
    dists = [init] * (N+1)
    dists[1] = 0

    while pq:
        w, n = heapq.heappop(pq)

        # 이전보다 더 적은 경로로 온 적이 있을 경우
        if dists[n] < w:
            continue 

        for next_w, next_n in g[n]:
            next_weight = w + next_w

            # 배달 갈 수 없을 경우
            if next_weight > K:
                continue

            # 이전보다 더 적은 경로로 온 적이 없을 경우
            if dists[next_n] < next_weight:
                continue

            dists[next_n] = next_weight
            heapq.heappush(pq,(next_weight,next_n))

    answer = len([x for x in dists if x <= K])

    return answer


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))