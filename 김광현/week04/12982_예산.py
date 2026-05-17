# 문제: 예산
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer = 0
    count = 0
    for i in d:
        if answer + i > budget:
            return count
        answer += i
        count += 1
    return count