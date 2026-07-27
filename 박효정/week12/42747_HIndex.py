# 문제: H-Index
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42747
 # [성능 요약] 메모리: 11.2 MB 시간: 27.96 ms 

def solution(citations):
    answer = 0
    
    # 인용횟수 i (어차피 논문개수를 넘어갈 수 없음)
    for i in range(len(citations) + 1):
        cnt = 0
        
        # 논문들을 돌면서 현재 횟수보다 인용횟수가 큰지 검사
        for c in citations:
            if c >= i:
                cnt += 1
        
        # 현재 인용횟수보다 인용된 수가 크거나 같다면 갱신 
        if cnt >= i:
            answer = i
        
    return answer