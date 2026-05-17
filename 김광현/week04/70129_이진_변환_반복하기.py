# 문제: 이진 변환 반복하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    count = 0
    gone_zero = 0
    
    while s != "1":
        gone_zero += s.count("0")
        s  = s.replace("0", "")
        
        s = bin(len(s))[2:]
        count += 1
    return [count, gone_zero]