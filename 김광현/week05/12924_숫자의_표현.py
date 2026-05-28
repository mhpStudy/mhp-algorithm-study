# 문제: 숫자의 표현
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    count = 0
    
    for i in range(1, n + 1):
        total = 0
        
        for j in range(i, n + 1):
            total += j
            
            if total == n:
                count += 1
                break
            
            if total > n:
                break
    return count