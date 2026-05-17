 # [성능 요약] 메모리: 9.25 MB 시간: 0.66 ms 

def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t)-l+1):
        if t[i:i+l] <= p:
            answer += 1
    return answer