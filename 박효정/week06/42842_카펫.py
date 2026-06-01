# 문제: 카펫
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    
    # yellow 기준으로 brown을 구할 것
    # 높이는 1부터 yellow개수까지 전부 확인
    for h in range(1, yellow + 1):
        # yellow가 높이로 나눠진다면 (직사각형 형태라면)
        if yellow % h == 0:
            # 너비는 yellow // h 
            w = yellow // h

            # 카펫의 너비와 높이는 각각 + 2
            carpet_w = w + 2
            carpet_h = h + 2
            
            # yellow 기준으로 brown을 계산했을 때 맞다면
            if 2 * carpet_w + 2 * carpet_h - 4 == brown:
                return [carpet_w, carpet_h]