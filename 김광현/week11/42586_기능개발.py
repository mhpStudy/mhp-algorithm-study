# 먼저 각 작업이 얼마나 시간이 걸리는지를 lst에 저장하기
def solution(progresses, speeds):
    n = len(progresses)
    time = [0] * n
    for i in range(n):
        j = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            j += 1
        if i != 0 and time[i-1] > j:
            time[i] = time[i-1]
        else:
            time[i] = j
            
    answer = []
    i = 0
    j = 1
    while i < (n - 1):
        if time[i] == time[i + 1]:
            i += 1
            j += 1
        else:
            answer.append(j)
            i += 1
            j = 1
    answer.append(j)
    
    return answer