# 문제: 다음 큰 숫자
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = bin(n).count("1")
    
    while True:
        n += 1
        if bin(n).count("1") == answer:
            return n