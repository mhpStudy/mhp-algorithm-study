# 문제: 짝지어 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for i in s:
        if stack and stack [-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if stack:
        return 0
    else:
        return 1