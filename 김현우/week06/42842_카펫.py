# 문제: 카펫
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    w, h = 0, 0
    # brown//2+2 = w+h
    # (w-2)*(h-2) = yellow
    while True:
        h += 1
        w = brown//2+2-h
        if (w-2)*(h-2) == yellow: break
    return [w,h]
