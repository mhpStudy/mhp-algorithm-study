# 문제: 최대공약수와 최소공배수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12940

def gcd(x, y):  # 유클리드 호제법
    while y:
        x, y = y, x%y
    return x

def lcm(x, y): return x*y/gcd(x, y)

def solution(n, m): return [gcd(n, m), lcm(n, m)]