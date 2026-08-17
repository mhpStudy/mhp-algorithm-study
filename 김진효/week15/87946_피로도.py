# [성능 요약] 메모리: 11.5 MB 시간: 17.64 ms 

def solution(k, dungeons):
    answer = 0

    n = len(dungeons)
    visited = [False] * n 

    def recur(cnt, remain):
        nonlocal answer

        answer = max(answer, cnt)

        if cnt == n+1:
            return

        for j in range(n):
            # 들리지 않았고, 최소 필요 피로도 충족할 경우
            if not visited[j] and remain >= dungeons[j][0]:
                visited[j] = True
                recur(cnt+1, remain-dungeons[j][1])
                visited[j] = False

    recur(0,k)

    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))