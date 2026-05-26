# 문제: 이상한 문자 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    cnt = 0
    for a in s:
        if a==' ':
            answer += ' '
            cnt = 0
            continue
        if cnt%2:
            answer += a.lower()
        else:
            answer += a.upper()
        cnt += 1
    return answer
