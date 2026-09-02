# [성능 요약] 메모리: 88.3 MB 시간: 4575.92 ms 

# 멀티소스 다익스트라
# 한 번의 다익스트라에서 모든 출입구를 시작 정점으로 두고 실행
# 참고: 2022 테크 여름인턴십 코딩테스트 해설: https://tech.kakao.com/posts/530

# 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함
# intensity(휴식 없이 이동해야하는 중 가장 긴 시간)이 최소가 되도록

# 노드 수(n), 등산로(paths) - [i, j, w] , 출입구(gates), 산봉우리(summits)
# return [산봉우리의 번호, intensity의 최솟값]

import heapq

def solution(n, paths, gates, summits):

    # 경로 저장
    g = [[] for _ in range(n+1)]
    for i, j, w in paths:
        g[i].append((w,j))
        g[j].append((w,i))

    init =  50000 * 10000000
    pq = [(0, start) for start in gates]
    intensity = [init] * (n+1) # 다익스트라를 응용하여 intensity를 기록해나갈 거임

    # 시작점 기록
    for start in gates:
        intensity[start] = 0

    while pq:
        cur_d,cur_node = heapq.heappop(pq)

        # 산봉우리 연속 방문 방지
        if cur_node in summits:
            continue

        # 이전에 더 적은 경로로 온 적이 있다면
        if intensity[cur_node] < cur_d:
            continue

        for next_d, next_n in g[cur_node]:

            # 이전에 더 적은 경로로 온 적이 있는 경우
            if intensity[next_n] <= max(intensity[cur_node],next_d):
                continue

            heapq.heappush(pq,(next_d,next_n))
            intensity[next_n] = max(intensity[cur_node],next_d)
            
    # 도착점들의 intensity 를 보고 min을 찾으면 된다 -> [산봉우리의 번호, intensity의 최솟값]
    # 같은 intensity 일 경우 산봉우리의 번호가 낮은 거
    min_v = init
    min_s = n+1
    for s in summits:
        if intensity[s] == min_v and s < min_s:
            min_s = s
        elif intensity[s] < min_v:
            min_v = intensity[s]
            min_s = s

    return [min_s, min_v]

# print(solution())
# print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1,3],[5]))
# print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2,3,4]))
print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3,7],[1,5]))
 