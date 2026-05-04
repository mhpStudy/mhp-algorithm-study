 # [성능 요약] 메모리: 9.08 MB 시간: 1.24 ms 

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer