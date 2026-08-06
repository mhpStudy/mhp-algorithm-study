# 문제: 귤 고르기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/138476
 # [성능 요약] 메모리: 23.2 MB 시간: 15.74 ms 

def solution(k, tangerine):
    counts = {}
    
    # tangerine을 돌면서 해당 숫자가 있다면 개수 추가하고, 없다면 key 새로 생성 
    for t in tangerine:
        counts[t] = counts.get(t, 0) + 1
    
    # 개수 많은 순서대로 정렬 
    li = sorted(counts.values(), reverse = True)
    
    cnt = 0 # 담은 귤의 수
    answer = 0 # 종류 수
    
    for i in li:
        cnt += i # 담고
        answer += 1 # 종류수 카운트
        if cnt >= k: # k보다 많아지면 중단
            break
    
    return answer