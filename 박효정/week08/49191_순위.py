# 문제: 순위
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/49191

# 다시보기
def solution(n, results):
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for win, lose in results:
        graph[win][lose] = True

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] and graph[k][b]:
                    graph[a][b] = True

    answer = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, n + 1):
            if i == j:
                continue

            if graph[i][j] or graph[j][i]:
                count += 1

        if count == n - 1:
            answer += 1

    return answer