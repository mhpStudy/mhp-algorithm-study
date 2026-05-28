# 문제: 최소직사각형
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    w = 0
    h = 0
    
    for a, b in sizes:
        big = max(a, b)
        small = min(a, b)
        
        w = max(w, big)
        h = max(h, small)
    
    return w * h
