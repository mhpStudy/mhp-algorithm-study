# 문제: 선인장 숨기기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/468379

from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1
    
    # 각 칸에 비가 내리는 시간 저장
    rain = [[INF] * n for _ in range(m)]

    for time, (r, c) in enumerate(drops, start=1):
        rain[r][c] = time

    # row_min[r][c]
    # = rain[r][c] ~ rain[r][c+w-1] 중 최솟값
    row_min = [[0] * (n - w + 1) for _ in range(m)]

    for r in range(m):
        dq = deque() # 현재 행에서 최솟값 후보의 열 번호를 저장할 덱

        for c in range(n): # 현재 행 왼쪽부터 확인
            while dq and rain[r][dq[-1]] >= rain[r][c]:
                # 현재 값보다 크거나 같은 기존 후보는
                # 앞으로 최솟값이 될 수 없으므로 제거
                dq.pop()
                
            # 현재 열 번호를 최솟값 후보로 추가
            dq.append(c)
            
            # 현재 창문범위보다 왼쪽에 있는 후보 제거
            if dq[0] <= c - w:
                dq.popleft()
                
            # 창문 길이가 w가 된 순간부터 최솟값 기록 시작
            if c >= w - 1:
                # c-w+1은 현재 창문의 시작 열 번호
                # 그 위치에 현재 창문의 최솟값을 기록
                row_min[r][c - w + 1] = rain[r][dq[0]]

    best_time = -1
    answer = (0, 0)

    # row_min을 세로 방향으로 h칸씩 보면서 최솟값 계산
    for c in range(n - w + 1):
        # 현재 열에서 최솟값 후보의 행 번호 저장
        dq = deque()
        
        # 현재 열 c에 있는 row_min의 모든 행 확인
        for r in range(m):
            # 현재 값보다 크거나 같은 기존 후보를 뒤에서 제거
            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()
            
            # 현재 행 번호를 최솟값 후보로 추가
            dq.append(r)
            
            # 현재 창문 범위를 벗어난 후보 제거
            if dq[0] <= r - h:
                dq.popleft()

            # 세로 창문이 h만큼이 된 순간부터 기록
            if r >= h - 1:
                # 가장 위 좌표: r - h + 1
                top = r - h + 1
                
                # 현재 h x w 구역의 최솟값
                current_time = row_min[dq[0]][c]
                
                # 더 늦게 비를 맞거나, 같은 시간이면 더 위쪽/왼쪽 좌표 선택
                if current_time > best_time or (
                    current_time == best_time and (top, c) < answer):
                    best_time = current_time
                    answer = (top, c)

    return list(answer)                                                           