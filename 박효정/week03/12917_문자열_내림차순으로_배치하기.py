# 문제: 문자열 내림차순으로 배치하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):

    ls = list(s)
    
    for j in range(len(s)):
        for i in range(len(s)-1):
            if ls[i] < ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i] 
    
    return ''.join(ls)

    # return ''.join(sorted(s, reverse=True))