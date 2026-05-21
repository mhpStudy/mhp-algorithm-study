# 문제: 크기가 작은 부분 문자열
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    
    n = len(p)
    p_num = int(p)
    for i in range(len(t)-n+1):
        num = int(t[i:i+n])
        if num <= p_num:
            answer += 1
    
    return answer