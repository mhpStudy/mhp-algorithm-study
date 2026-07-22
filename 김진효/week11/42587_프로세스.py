 # [성능 요약] 메모리: 11.5 MB 시간: 0.23 ms 

# 우선 순위가 높은거 먼저 실행
from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([])
    # 인덱스랑 프로세스 우선순위 저장
    for idx, p in enumerate(priorities):
        q.append((idx,p))

    while q:
        high_v = max(q,key=lambda x:x[1])[1]

        # 우선순위 낮으면 꺼내고 다시 뒤로
        while high_v != q[0][1]:
            cur = q.popleft()
            q.append(cur)

        high_p = q.popleft()
        answer += 1

        if high_p[0] == location:
            break
        

    return answer


print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
