# 문제: 완주하지 못한 선수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    count = {}

    for name in participant:
        count[name] = count.get(name, 0) + 1


    for name in completion:
        count[name] -= 1


    for name, c in count.items():
        if c > 0:
            return name