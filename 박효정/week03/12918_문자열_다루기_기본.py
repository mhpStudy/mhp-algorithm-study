# 문제: 문자열 다루기 기본
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    num = set(str(i) for i in range(0, 10))

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in num:
                return False
    else:
        return False        

    return True
