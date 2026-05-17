# 문제: 최솟값 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))