# 문제: 기능개발
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    pg = deque(progresses)
    sp = deque(speeds)
    
    
    # 차있는동안 계속 
    while pg:
        
        # 모든 작업을 하루만큼 진행한다
        for i in range(len(pg)):
            pg[i] += sp[i]
        
        # 맨 앞 작업이 완료되었을 때만 배포 가능 
        if pg[0] >= 100:
            cnt = 0
            
            # 앞에서부터 연속으로 완료된 기능을 함께 배포 
            while pg and pg[0] >= 100:
                pg.popleft()
                sp.popleft()
                cnt += 1
        
            answer.append(cnt)
    
    return answer