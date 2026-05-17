# 문제: 최대공약수와 최소공배수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    double = n * m
    
    a, b = n ,m
    while b:
        a, b = b, a % b
    
    gcd = a
    lcm = double // gcd
    
    answer = [gcd, lcm]
    
    return answer