# 문제: 문자열 다루기 기본
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
        