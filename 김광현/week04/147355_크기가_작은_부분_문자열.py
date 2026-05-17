# 문제: 크기가 작은 부분 문자열
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    size = len(p)
    target = int(p)
    answer = 0
    
    for i in range(len(t) - size + 1):
        a = int(t[i:i + size])
        if a <= target:
            answer += 1
    return answer