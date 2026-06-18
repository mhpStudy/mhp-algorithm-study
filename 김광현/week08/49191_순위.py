# 문제: 순위
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/49191

from collections import deque

def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]

    for a, b in results:
        win[a].append(b)
        lose[b].append(a)

    answer = 0

    for i in range(1, n+1):
        # i가 이긴 모든 사람 찾기
        beat = set()
        q = deque([i])
        while q:
            now = q.popleft()
            for next in win[now]:
                if next not in beat:
                    beat.add(next)
                    q.append(next)

        # i가 진 모든 사람 찾기
        lost_to = set()
        q = deque([i])
        while q:
            cur = q.popleft()
            for next in lose[cur]:
                if next not in lost_to:
                    lost_to.add(next)
                    q.append(next)

        if len(beat) + len(lost_to) == n - 1:
            answer += 1

    return answer