# 문제: 내적
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    for A,B in zip(a,b):
        answer += A*B
    return answer