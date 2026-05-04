 # [성능 요약] 메모리: 9.27 MB 시간: 0.20 ms 

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    # for x,y in zip(a,b):
    #     answer += x*y
    return answer