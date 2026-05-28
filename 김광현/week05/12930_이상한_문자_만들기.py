# 문제: 이상한 문자 만들기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    idx = 0
    
    for i in s:
        if i == " ":
            answer += " "
            idx = 0
        else:
            if idx % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            idx += 1
            
    return answer