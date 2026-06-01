# 문제: 콜라 문제
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    while a <= n:
        # 교환 횟수
        exchanged = n // a
        # 누적 콜라 수 
        answer += exchanged * b
        # 다음 턴의 빈 병 수
        n = n % a + exchanged * b
    
    return answer