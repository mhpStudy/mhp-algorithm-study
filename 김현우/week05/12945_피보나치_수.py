# 문제: 피보나치 수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12945

# from functools import lru_cache

# @lru_cache(None)
# def fibo(n):
#     if n==0: return 0
#     if n==1: return 1
#     return fibo(n-1)+fibo(n-2)

# def solution(n): return fibo(n)%1234567


def solution(n):
    MOD = 1234567

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD

    return b
