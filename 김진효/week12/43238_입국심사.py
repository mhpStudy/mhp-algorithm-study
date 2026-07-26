# 기다리는 사람을 빈 곳에 넣어보려면 오래걸림
# 이 시간에 기다리는 사람을 다 심사할 수 있을까의 관점으로 다가가보자

"""
 # 이분 탐색 이용
 # [성능 요약] 메모리: 15.6 MB 시간: 347.90 ms 
"""
# 최대로 걸리는 시간은 가장 오래 걸리는 time * n
# 각 시간에 다 심사를 할 수 있는 지 판단하면서 시간 범위를 점점 좁혀가보자
def solution(n, times):
    answer = 0

    # 정렬
    times.sort()

    # 범위
    left = 0
    right = times[-1] * n

    # 중간지점
    while left <= right:
        mid = (left+right) // 2

        # 처리 할 수 사람 수 검토
        processed = 0
        for t in times:
            processed += mid // t

        # 처리 가능할 것 같으면 시간 줄이고 못할 것 같으면 늘려봐야함
        if processed >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

# 시간초과
# def solution(n, times):
#     min_v = min(times)
#     time = 0
#     while True:
#         time += min_v

#         # 첫 시작은 대기시간 X
#         processed = len(times)
#         for t in times:
#             # 심사관이 몇 명을 심사할 수 있을지 검토
#             if t <= time:
#                 processed += time // t - 1

#         if processed >= n:
#             return time


print(solution(6,[7,10])) # 28
print(solution(6,[10,3,7])) # 9 
print(solution(3,[1,2])) # 2