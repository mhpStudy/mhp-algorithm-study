# 문제: 게임 맵 최단거리
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/1844
 # [성능 요약] 메모리: 11.1 MB 시간: 6.58 ms 

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:           # 범위 안
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:  # 길 + 미방문
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist[n-1][m-1]    # 도달 못 했으면 -1 그대로