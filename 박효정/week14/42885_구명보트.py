# 문제: 구명보트
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42885
 # [성능 요약] 메모리: 11.8 MB 시간: 8.08 ms 

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort() # 오름차순 정렬
    dq = deque(people)
    
    while dq:
        right = dq.pop() # 가장 무거운 사람
        
        if not dq: # 마지막 사람이라면 태우고 종료
            answer += 1
            break
        
        left = dq[0] # 가장 가벼운 사람
        
        # 가장 가벼운 사람 + 가장 무거운 사람이 limit보다 작다면 태움
        if right + left <= limit:
            dq.popleft()
        # 크다면 right 혼자 탐
        answer += 1
        
    return answer