# 문제: 수박수박수박수박수박수?
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    for i in range(n):
        if answer[-1:]!="수":
            answer += "수"
        else: answer += "박"
    return answer


def water_melon(n):
    str = "수박"*n
    return str[:n]