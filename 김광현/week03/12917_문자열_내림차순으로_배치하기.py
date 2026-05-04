# 문제: 문자열 내림차순으로 배치하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    a = list(s)
    a.sort(reverse = True)
    for i in a:
        answer += i
    return answer