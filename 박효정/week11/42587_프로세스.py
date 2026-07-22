# 문제: 프로세스
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = []
    
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
    
    q = deque(queue)
    
    while q:
        now = q.popleft()
        
        flag = -1
        for l, p in q:
            if p > now[1]:
                q.append(now)
                flag = 1
                break
        
        if flag == 1:
            continue
        
        else:
            answer += 1
            
        if now[0] == location:
            break
            
    return answer