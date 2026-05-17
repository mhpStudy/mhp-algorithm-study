# 문제: 올바른 괄호
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
            
    if len(stack) == 0:
        return True
    else:
        return False