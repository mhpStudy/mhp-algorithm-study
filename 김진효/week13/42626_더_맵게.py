'''
[성능 요약] 메모리: 52.6 MB 시간: 1643.10 ms 
[채점 결과] 정확성: 83.9, 효율성: 16.1, 합계: 100.0 / 100.0
'''
# 최소 힙 -> 부모 루트 < 자식 루트
# 루트 노드가 K 이상이면 끝
import heapq

def solution(scoville, K):
    answer = 0

    # 최소힙으로 변환
    heapq.heapify(scoville)

    while scoville[0] < K:

        # 만약 다 합쳐봤는데도 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(scoville) < 2:
            return -1 

        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville,x+y*2)
        answer +=1 

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2
print(solution([1, 2], 7)) # -1