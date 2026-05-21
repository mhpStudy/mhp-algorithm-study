# 문제: 이진 변환 반복하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    loop, removed = 0,0
    while s != "1":
        loop += 1
        cnt = 0
        for i in s:
            if i=='0':
                removed += 1
            else: cnt += 1
        s = bin(cnt)[2:]
    return [loop, removed]
