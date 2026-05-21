# 문제: 예산
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    money = 0
    for m in sorted(d):
        money += m
        if money <= budget:
            answer += 1
        else: return answer
    return answer

