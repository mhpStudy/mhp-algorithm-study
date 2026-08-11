# [성능 요약] 메모리: 12.4 MB 시간: 8.83 ms 
# 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없음
from collections import deque

def solution(people, limit):
    answer = 0

    q = deque(sorted(people,reverse=True))

    while q:
        s = 0
        s += q.popleft()
        if q and q[-1] + s <= limit:
            s += q.pop()

        answer += 1

    return answer

print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))