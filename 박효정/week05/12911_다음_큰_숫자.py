# 문제: 다음 큰 숫자
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    # 1. n의 1 개수 세기
    num = bin(n).count('1')
    
    # 2. 하나씩 올려가며 같은 수 찾기
    for i in range(n+1, 1000001):
        if bin(i).count('1') == num:
            answer = i
            break
        
    return answer