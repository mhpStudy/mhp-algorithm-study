# 문제: 더 맵게
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42626
 # [성능 요약] 메모리: 52.6 MB 시간: 1636.23 ms 

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K: # 최솟값이 K보다 클때까지
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    
    return answer