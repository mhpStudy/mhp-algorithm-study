# 문제: 피보나치 수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    a, b = 0, 1
    
    for i in range(2, n + 1):
        a, b = b, (a + b) % 1234567

    return b