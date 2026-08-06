'''
최소 힙 이용
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

#     return answer


'''
deque를 2개 둬서 푸는 방법
[성능 요약] 메모리: 67.6 MB 시간: 531.93 ms 
[채점 결과] 정확성: 83.9, 효율성: 16.1, 합계: 100.0 / 100.0
'''
# from collections import deque

# def solution(scoville, K):
#     # 스코빌 담은 큐와 mix 한 값들을 담은 큐
#     sq = deque(sorted(scoville))
#     mq = deque()

#     cnt = 0
#     while len(sq) + len(mq) > 1:

#         x = 0
#         y = 0

#         # 첫 번째 작은 요소
#         if sq and (not mq or sq[0] < mq[0]):
#             x = sq.popleft()
#         else:
#             x = mq.popleft()

#         # 스코빌 지수 K 이상
#         if x >= K:
#             return cnt

#         # 두 번째 작은 요소
#         if sq and (not mq or sq[0] < mq[0]):
#             y = sq.popleft()
#         else:
#             y = mq.popleft()

#         mq.append(x + y*2)

#         cnt += 1

#     # 혹시 남아있는 요소 하나가 K 를 넘었을 경우 cnt 반환해야함
#     if (sq and sq[0] >= K) or (mq and mq[0] >= K):
#         return cnt
        
#     return -1

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2
print(solution([1, 2], 7)) # -1