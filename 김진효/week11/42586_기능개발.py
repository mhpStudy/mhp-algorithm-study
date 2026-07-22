 # [성능 요약] 메모리: 11.6 MB 시간: 0.03 ms 

# stack 이용
def solution(progresses, speeds):
    answer = []
    s = progresses[::-1]
    day = 0
    speed = 0

    while s:
        day += 1
        s[-1] += speeds[speed]
        
        # 완료 되면 빼내기
        complete = 0
        while s and s[-1] >= 100:
            s.pop()
            complete += 1
            if s:
                speed += 1
                s[-1] += day * speeds[speed]

        if complete != 0:
           answer.append(complete) 

   
    return answer


print(solution([93,30,55],[1,30,5]))