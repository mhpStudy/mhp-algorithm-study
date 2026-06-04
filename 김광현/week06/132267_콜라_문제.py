# 문제: 콜라 문제
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        new_coke = (n // a) * b
        
        answer += new_coke
        
        n = (n % a) + new_coke
        
    return answer