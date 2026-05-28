# 문제: 3진법 뒤집기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    arr = []
    
    while n > 0:
        arr.append(str(n % 3))
        n //= 3
        
    return int(''.join(arr), 3)