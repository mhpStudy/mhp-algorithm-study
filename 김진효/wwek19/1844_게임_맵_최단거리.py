# [성능 요약] 메모리: 11.4 MB 시간: 6.32 ms 

# BFS
# 0 = 벽, 도착지는 (n,m)
from collections import deque
def solution(maps):
    answer = -1
    
    row = len(maps)
    col = len(maps[0])

    visited = [[0] * col for _ in range(row)]

    q = deque([(0,0)])
    visited[0][0] = 1

    while q:
        i,j = q.popleft()

        if i == row - 1 and j == col - 1:
            print(visited)
            return visited[i][j]
        
        for di,dj in [0,1],[1,0],[0,-1],[-1,0]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < row and 0 <= nj < col and visited[ni][nj] == 0 and maps[ni][nj] != 0:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))