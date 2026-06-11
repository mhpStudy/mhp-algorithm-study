# 문제: 선인장 숨기기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/468379

def get_safe_spots(m, n, h, w, drops, mid):
    # 1. mid번째 비까지 내린 상태를 격자에 표시 (1 = 비 맞음, 0 = 안전함)
    # 누적 합 계산을 쉽게 하기 위해 패딩(+1)을 줌
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(mid):
        r, c = drops[i]
        grid[r + 1][c + 1] = 1

    # 2. 2차원 누적 합 계산 (구간 내의 비 맞은 칸 수를 1초 만에 구하기 위함)
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            grid[r][c] += grid[r - 1][c] + grid[r][c - 1] - grid[r - 1][c - 1]

    possible_spots = []

    # 3. 모든 가능한 선인장 좌상단 시작점(r, c)을 탐색
    # 위에서부터, 왼쪽에서부터 순회하므로 자동 정렬 효과
    for r in range(1, m - h + 2):
        for c in range(1, n - w + 2):
            # 선인장이 차지하는 우하단 좌표
            end_r, end_c = r + h - 1, c + w - 1

            # 누적 합 공식을 이용해 선인장 영역(h x w) 내의 '비 맞은 칸 수' 도출
            rain_count = (grid[end_r][end_c]
                          - grid[r - 1][end_c]
                          - grid[end_r][c - 1]
                          + grid[r - 1][c - 1])

            # 비 맞은 칸이 0개라면 완벽한 안전 구역!
            if rain_count == 0:
                possible_spots.append((r - 1, c - 1))  # 원래 좌표계로 복원하여 저장

    return possible_spots


def solution(m, n, h, w, drops):
    # 이분 탐색 초기화
    left = 0
    right = len(drops)
    best_spots = []

    while left <= right:
        mid = (left + right) // 2

        # mid번째 비까지 내렸을 때 안전 구역이 존재하는가?
        spots = get_safe_spots(m, n, h, w, drops, mid)

        if spots:
            # 안전 구역이 존재한다면, 이 구역들을 정답 후보로 저장해두고
            best_spots = spots
            # 비를 더 많이 내려봄 (더 오래 버티는 순간을 찾기 위해)
            left = mid + 1
        else:
            # 안전 구역이 하나도 없다면, 비를 너무 많이 내린 것이므로 줄임
            right = mid - 1

    # best_spots에는 '가장 오래 버텼을 때'의 안전 구역들이 담겨 있음.
    # 탐색 순서상 가장 상단-좌측이 0번째 인덱스에 위치함.
    return [best_spots[0][0], best_spots[0][1]]



############################################


from collections import deque


def get_sliding_window_min(arr, k):
    """
    1차원 배열 arr에서 크기가 k인 슬라이딩 윈도우의 최솟값들을 반환하는 함수.
    모노토닉 데크(Monotonic Deque)를 사용하여 O(N)의 시간 복잡도를 보장합니다.
    """
    res = []
    dq = deque()

    for i, val in enumerate(arr):
        # 1. 윈도우의 범위를 벗어난 인덱스 제거
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # 2. 데크의 끝에서부터, 현재 값(val)보다 크거나 같은 값들은 모두 제거
        #    (앞으로 윈도우 안에서 절대 최솟값이 될 수 없으므로 가지치기)
        while dq and arr[dq[-1]] >= val:
            dq.pop()

        # 3. 현재 인덱스 추가
        dq.append(i)

        # 4. 윈도우가 가득 차기 시작한 시점부터 맨 앞(최솟값)의 값을 결과에 추가
        if i >= k - 1:
            res.append(arr[dq[0]])

    return res


def solution(m, n, h, w, drops):
    # 1. 격자 초기화: 비가 내리지 않는 칸은 무한대(INF)로 설정
    INF = len(drops) + 1
    grid = [[INF] * n for _ in range(m)]

    # 빗방울이 떨어지는 시간을 1부터 시작하는 순서로 기록
    for idx, (r, c) in enumerate(drops):
        # 동일한 위치에 비가 여러 번 온다면 처음 맞은 시간이 기준이 됨
        if grid[r][c] == INF:
            grid[r][c] = idx + 1

    # 2. 가로 방향(w) 슬라이딩 윈도우 최솟값 구하기
    row_mins = []
    for r in range(m):
        row_mins.append(get_sliding_window_min(grid[r], w))

    # 3. 세로 방향(h) 슬라이딩 윈도우 최솟값 구하기
    cols = n - w + 1
    rows = m - h + 1
    final_mins = [[0] * cols for _ in range(rows)]

    for c in range(cols):
        # 각 열(Column) 데이터를 1차원 배열로 추출하여 세로 최솟값 계산
        col_data = [row_mins[r][c] for r in range(m)]
        col_res = get_sliding_window_min(col_data, h)
        for r in range(rows):
            final_mins[r][c] = col_res[r]

    # 4. 가장 늦게 젖는(최솟값들 중 최댓값) 구역의 상단-좌측 좌표 찾기
    max_safe_time = -1
    best_r, best_c = -1, -1

    # 행, 열을 위에서부터, 왼쪽에서부터 순회하므로
    # 조건 만족 시 자동으로 가장 상단-좌측 좌표가 최적해가 됨
    for r in range(rows):
        for c in range(cols):
            if final_mins[r][c] > max_safe_time:
                max_safe_time = final_mins[r][c]
                best_r, best_c = r, c

    return [best_r, best_c]