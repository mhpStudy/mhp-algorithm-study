# 문제: 가장 가까운 같은 글자
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    save = dict()
    for idx, char in enumerate(s):
        if char in save:
            answer.append(idx-save[char])
            save[char] = idx
        else:
            save[char] = idx
            answer.append(-1)
    return answer
