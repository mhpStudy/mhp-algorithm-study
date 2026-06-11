# m개의 행과 n개의 열 -> 사막 지도
# 가로 w, 세로 h 크기의 선인장 구역을 조성하려고 함
# 연속된 w h 크기의 격자, 회전 분가

# 비구름은 미리 정해진 순서대로 여러 칸에 비 뿌림
# 이때 빗방울이 처음으로 선인장 구역에 포함된 칸에 떨어졌을 때
# 그 시점이 선인장이 처음으로 비를 맞는 순간
# 선인장이 비 늦게 맞도록 하자

# 선인장이 비를 맞지 않도록 하면 최선
# 가장 늦게 맞는게 여러 개라면, 그중 가장 위쪽 행, 왼쪽 열

# 아이디어를 생각해보자
# 일단 가장 위 왼쪽이라는 것을 보니까 for문으로 찾으면 좋을듯
# 내 생각에는 drops에서 가능한 횟수를 찾고, for문으로 그 중에서 찾기

# 아니면 어차피 개수가 적으니까

from collections import deque

def solution(m, n, h, w, drops):

    INF = m * n + 1
    
    grid = [[INF]*n for _ in range(m)]
    
    x = 1
    for i, j in drops:
        grid[i][j] = x
        x += 1
    
    
    result = [[] for _ in range(m)]
    
    # 우선 가로 슬라이딩 윈도우를 구해보자
    for i in range(m):
        q = deque()
        for j in range(n):
            if q and q[0] <= j - w:
                q.popleft()
            while q and grid[i][q[-1]] > grid[i][j]:
                q.pop()
            q.append(j)
            if j >= w - 1:
                result[i].append(grid[i][q[0]])
            
    final = [[] for _ in range(m-h+1)]
    
    for i in range(n - w + 1):
        q = deque()
        for j in range(m):
            if q and q[0] <= j - h:
                q.popleft()
            while q and result[q[-1]][i] > result[j][i]:
                q.pop()
            q.append(j)
            if j >= h - 1:
                final[j-h+1].append(result[q[0]][i])
                
    max_val = -1
    answer = [0, 0]
    
    for i in range(m - h + 1):
        for j in range(n - w + 1):
            val = final[i][j]
            
            if val > max_val:
                max_val = val
                answer = [i, j]
    
    return answer