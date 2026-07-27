# 문제: 프로세스
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    # 1. 큐 초기화: (초기 인덱스, 우선순위) 형태로 deque 생성
    queue = deque(enumerate(priorities))
    
    # 실행된 프로세스의 횟수를 셀 변수
    answer = 0 
    
    # 2. 큐에 프로세스가 남아있는 동안 계속 반복
    while queue:
        # 대기 큐에서 가장 앞에 있는 프로세스를 꺼냄
        current = queue.popleft()
        
        # 3. 큐에 남아있는 프로세스 중 현재 꺼낸 프로세스보다 우선순위가 높은 게 있는지 확인
        # any() 함수는 조건에 맞는 요소가 하나라도 있으면 True를 반환합니다.
        # current[1]은 현재 프로세스의 우선순위, q[1]은 큐에 있는 다른 프로세스들의 우선순위입니다.
        if any(current[1] < q[1] for q in queue):
            # 우선순위가 더 높은 게 있다면, 방금 꺼낸 프로세스를 다시 맨 뒤로 넣음
            queue.append(current)
        else:
            # 우선순위가 더 높은 게 없다면 프로세스를 실행함
            answer += 1 # 실행 횟수 1 증가
            
            # 방금 실행한 프로세스의 초기 인덱스(current[0])가 우리가 찾던 location과 같다면?
            if current[0] == location:
                # 현재까지의 실행 횟수를 반환하고 함수 종료
                return answer
