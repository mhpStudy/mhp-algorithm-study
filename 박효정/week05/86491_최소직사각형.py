# 문제: 최소직사각형
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    # 1. 더 긴쪽을 가로로 만들어서 배치하자
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
    
    # 2. 가장 긴 가로와 가장 긴 세로를 찾자
    a, b = 0, 0
    for s in sizes:
        if s[0] > a:
            a = s[0]
        if s[1] > b:
            b = s[1]
            
    return a * b