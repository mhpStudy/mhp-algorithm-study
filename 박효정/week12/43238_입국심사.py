# 문제: 입국심사
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/43238
 # [성능 요약] 메모리: 15.6 MB 시간: 376.42 ms 

def solution(n, times):
    left = 1 # 소요시간 1분부터 시작
    right = times[-1] * n # 가장 느린사람이 혼자 했을때
    
    while left < right:
        mid = (left+right) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t # 몇명까지 가능한지 계산
        
        if cnt >= n:
            right = mid 
        else:
            left = mid + 1
    
    return left