# 문제: 크기가 작은 부분 문자열
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):    # int 안써도 가능
            answer += 1
    return answer