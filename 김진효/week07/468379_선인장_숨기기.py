
'''
시간초과 (카카오 못가겟다..)
'''

# 선인장 구역을 (0,0)에서부터 (m-1, n-1) 구역까지 돌면서
# 제일 늦은 순서 갱신 (선인장 구역내에서 가장 늦게 맞을 수 있는지 판별)
# 여러개일경우 좌상단을 반환하라고 했으므로 0,0 부터 →, ↓ 탐색하면서 아예 안맞는 영역 찾으면 break

# def solution(m, n, h, w, drops):
#     answer = []

#     drop_length = len(drops)

#     max_v = 0

#     # 배열에 비가 떨어지는 순서 채워놓기
#     arr = [[0] * n for _ in range(m)]
#     for i in range(len(drops)):
#         arr[drops[i][0]][drops[i][1]] = i + 1

#     # 지도 배열
#     for i in range(m-h+1):
#         for j in range(n-w+1):
#             # 영역 내 순서를 판단할 temp 변수
#             temp = drop_length + 1
#             #  선인장 배열
#             for k in range(w):
#                 for l in range(h):
#                     # 비가 오는 영역만 판별
#                     if arr[i+l][j+k] != 0:
#                         temp = min(temp,arr[i+l][j+k])

#             # 갱신이 안된 초기화 상태라면 이 영역은 비가 오지 않는 영역이라는 소리!            
#             if temp == drop_length + 1:
#                 return [i, j]

#             if max_v < temp:
#                 max_v = temp
#                 answer = [i,j]

#     return answer

from collections import deque

'''
슬라이딩 윈도우
가로 한번 돌리고 나온걸 세로로 돌리면 겹치는 영역까지 커버 가능
일단 deque 에 다 집어넣고 min 으로 찾으려다보니 또 다시 터졌다.. ;)
아무래도 deque 에 다 집어넣고 다시 비교를 하다보니 결국 다 도는거나 매한가지..
'''
# def solution(m, n, h, w, drops):
#     default = 500000 ** 2 + 1 
#     arr= [[default] * n for _ in range(m)]
#     for order in range(len(drops)):
#         row = drops[order][0]
#         col = drops[order][1]
#         arr[row][col] = order + 1

#     # 가로 영역 슬라이딩 윈도우
#     w_window = [[0] * (n-w+1) for _ in range(m)]

#     for row in range(m):
#         # 가로가 1이라면 그대로
#         if w == 1:
#             w_window[row] = arr[row]
#         # 아니면 슬라이딩 윈도우 활용
#         else:
#             q = deque(arr[row][:w])
#             w_window[row][0] = min(q)
#             for col in range(1,n-w+1):
#                 q.popleft()
#                 q.append(arr[row][col+1])
#                 w_window[row][col] = min(q)

#     # 출력 확인용
#     # for i in range(m):
#     #     for j in range(n-w+1):
#     #         print(w_window[i][j],end=" ")
#     #     print()

#     # 세로 영역 슬라이딩 윈도우 
#     # (위에서 구한 걸 기준으로 윈도우 돌리면 겹치는 부분도 커버 된다)
#     h_window = [[0] * (n-w+1) for _ in range(m-h+1)]
#     for col in range(n-w+1):
#         # 넓이가 1이라면 그대로
#         if h == 1:
#             h_window = w_window
#         # 아니면 슬라이딩 윈도우 활용
#         else:
#             # 초기값 세팅
#             q = deque()
#             for init in range(h):
#                 q.append(w_window[init][col])
#             h_window[0][col] = min(q) 

#             for row in range(1,m-h+1):
#                 q.popleft()
#                 q.append(w_window[row+1][col])
#                 h_window[row][col] = min(q)

#     # 출력 확인용
#     # for i in range(m-h+1):
#     #     for j in range(n-w+1):
#     #         print(h_window[i][j],end=" ")
#     #     print()

#     max_v = 0
#     max_row = 0
#     max_col = 0
#     for i in range(m-h+1):
#         for j in range(n-w+1):
#             if h_window[i][j] == default:
#                     return [i,j]
#             if h_window[i][j] > max_v:
#                 max_v = h_window[i][j]
#                 max_row = i
#                 max_col = j

#     return [max_row,max_col]


'''
슬라이딩 윈도우
q 에는 좌표값을 저장해서 슬라이딩 배열을 채우는데, 이때 최솟값을 그때 그떄 비교해서 집어넣기
[성능 요약] 메모리: 161 MB 시간: 614.82 ms 
'''

from collections import deque

def solution(m, n, h, w, drops):
    default = len(drops) + 1
    arr= [[default] * n for _ in range(m)]
    for order in range(len(drops)):
        row = drops[order][0]
        col = drops[order][1]
        arr[row][col] = order + 1

    # 가로 영역 슬라이딩 윈도우
    w_window = [[0] * (n-w+1) for _ in range(m)]

    for row in range(m):
        q = deque()
        for col in range(n):
            # 영역을 벗어나는 값 제거하기
            if q and q[0] < col-w+1:
                q.popleft()

            # 앞의 값이 후보가 될 수 없을 것 같으면 꺼내야함
            while q and arr[row][q[-1]] > arr[row][col]:
                q.pop()

            # 앞에 정리 다 끝났다 싶으면 집어넣자
            q.append(col)

            # 영역 충족되는 시점부터는 기록해야함
            if col >= w-1: 
                w_window[row][col-w+1] = arr[row][q[0]]

    # 세로 영역 슬라이딩 윈도우
    h_window = [[0] * (n-w+1) for _ in range(m-h+1)]
    for col in range(n-w+1):
        q = deque()
        for row in range(m):
            # 영역을 벗어나는 값 제거하기
            if q and q[0] < row-h+1:
                q.popleft()

            # 앞의 값이 후보가 될 수 없을 것 같으면 꺼내야함
            while q and w_window[q[-1]][col] > w_window[row][col]:
                q.pop()

            # 앞에 정리 다 끝났다 싶으면 집어넣자
            q.append(row)

            # 영역 충족되는 시점부터는 기록해야함
            if row >= h-1: 
                h_window[row-h+1][col] = w_window[q[0]][col]

    # 이제 여기서 가장 늦게 맞는 영역 반환하면 된다
    max_v = 0
    max_row = 0
    max_col = 0
    for i in range(m-h+1):
        for j in range(n-w+1):
            if h_window[i][j] == default:
                    return [i,j]
            if h_window[i][j] > max_v:
                max_v = h_window[i][j]
                max_row = i
                max_col = j

    return [max_row,max_col]


print(solution(4,5,2,2,	[[0, 0], [3, 1], [1, 3], [2, 4], [1, 1], [2, 2], [2, 3], [0, 4]]))
print(solution(3,3,1,1,	[[0, 0], [0, 1], [0, 2], [1, 0]]))
print(solution(4,6,3,4,	[[1, 2]]))
print(solution(4,6,1,2,	[[0, 1], [0, 3], [0, 5], [1, 1], [1, 3], [1, 5], [2, 1], [2, 3], [2, 5], [3, 1], [3, 3], [3, 5]]))
print(solution(2,2,2,2,	[[0, 0], [0, 1], [1, 1], [1, 0]]))
print(solution(4,4,3,1,	[[2, 0], [1, 3], [3, 2], [0, 1]]))