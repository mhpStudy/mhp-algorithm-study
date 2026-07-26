 # [성능 요약] 메모리: 11.4 MB 시간: 0.08 ms 

def solution(citations):
    citations.sort()
    n = len(citations)

    for idx, c in enumerate(citations):
        # n-idx = c만큼 인용된 횟수
        if c >= n-idx:
            return n-idx

    return 0


# # print(solution([]))
# print(solution([3, 0, 6, 1, 5]))
# print(solution([4, 4, 4, 4, 4, 4]))
# print(solution([0, 1, 5, 2]))
# print(solution([10,9,8,6]))
# print(solution([1,3]))
# print(solution([0,0]))