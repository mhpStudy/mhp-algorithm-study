# 문제: 코딩 테스트 공부
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/118668

def solution(alp, cop, problems):

    target_alp = max(problem[0] for problem in problems)
    target_cop = max(problem[1] for problem in problems)

    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    INF = float('inf')

    # dp[a][c] = 알고력이 a이고 코딩력이 c인 상태에 도달하는 데 필요한 최소 시간
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]

    dp[alp][cop] = 0

    for a in range(alp, target_alp + 1):
        for c in range(cop, target_cop + 1):

            # 알고력 공부
            if a < target_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)

            # 코딩력 공부
            if c < target_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            # 문제 풀기
            for req_a, req_c, rwd_a, rwd_c, cost in problems:

                # 현재 능력치로 풀 수 있는지
                if a >= req_a and c >= req_c:

                    # 문제를 풀고 얻는 새로운 능력치
                    next_a = min(target_alp, a + rwd_a)
                    next_c = min(target_cop, c + rwd_c)

                    # 기존에 알고 있던 최소 시간 비교
                    dp[next_a][next_c] = min(dp[next_a][next_c], dp[a][c] + cost)

    return dp[target_alp][target_cop]



import heapq

def solution2(alp, cop, problems):
    target_alp = max(p[0] for p in problems)
    target_cop = max(p[1] for p in problems)

    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    INF = float('inf')

    dist = [
        [INF] * (target_cop + 1)
        for _ in range(target_alp + 1)
    ]

    dist[alp][cop] = 0

    heap = [(0, alp, cop)]

    while heap:
        cost, a, c = heapq.heappop(heap)

        if cost != dist[a][c]:
            continue

        if a == target_alp and c == target_cop:
            return cost

        # 알고력 공부
        if a < target_alp:
            na = a + 1

            if dist[na][c] > cost + 1:
                dist[na][c] = cost + 1
                heapq.heappush(heap, (cost + 1, na, c))

        # 코딩력 공부
        if c < target_cop:
            nc = c + 1

            if dist[a][nc] > cost + 1:
                dist[a][nc] = cost + 1
                heapq.heappush(heap, (cost + 1, a, nc))

        # 문제 풀기
        for req_a, req_c, rwd_a, rwd_c, p_cost in problems:

            if a >= req_a and c >= req_c:
                na = min(target_alp, a + rwd_a)
                nc = min(target_cop, c + rwd_c)

                if dist[na][nc] > cost + p_cost:
                    dist[na][nc] = cost + p_cost
                    heapq.heappush(heap,(cost + p_cost, na, nc))