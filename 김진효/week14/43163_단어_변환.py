# [성능 요약] 메모리: 11.3 MB 시간: 0.21 ms 
# 한 글자만 바꿀 수 있다면 갈 수 있는 경로
# BFS 로 풀어 보기

from collections import deque

def solution(begin, target, words):
    answer = 0

    q = deque([(begin,0)])
    visited = [False] * len(words)
    n = len(begin)

    while q:
        word, k = q.popleft()

        # 타겟 도착시 break
        if word == target:
            return k 

        for i in range(len(words)):
            diff_cnt = 0

            # 방문하지 않았으면 진행
            if not visited[i]:
                # 한 글자만 다른거 찾기
                for j in range(n):
                    if words[i][j] != word[j]:
                        diff_cnt +=1
                # 갈 수 있는 경로면
                if diff_cnt == 1:
                    visited[i] = True
                    q.append((words[i],k+1))

    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))