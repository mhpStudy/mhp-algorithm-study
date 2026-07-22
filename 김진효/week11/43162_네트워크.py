 # [성능 요약] 메모리: 11.5 MB 시간: 0.77 ms 

from collections import deque

# 굳이 인접 배열말고 0번 정점으로 해서
# 입력케이스 (1,1,0) 이대로 돌아보면 될 것 같은데
def solution(n, computers):
    answer = n

    visited = [False] * n
    visited[0] = True

    q = deque([i for i in range(n)])
    while q:
        now = q.popleft()
        visited[now] = True
        for i in range(n):
            if now == i:
                continue
            # 연결되어 있고 방문하지 않았다면
            if computers[now][i] == 1 and not visited[i]:
                visited[i] = True
                q.appendleft(i)
                answer -=1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4,[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]))
