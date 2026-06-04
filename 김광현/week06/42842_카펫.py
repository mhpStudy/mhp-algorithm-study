# 문제: 카펫
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for h in range(1, int(yellow ** 0.5) + 1):
        if yellow % h == 0:
            w = yellow // h

            if (w + 2) * (h + 2) - yellow == brown:
                return [w + 2, h + 2]