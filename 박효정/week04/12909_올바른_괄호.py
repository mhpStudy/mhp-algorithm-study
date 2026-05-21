# 문제: 올바른 괄호
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(st):
    
    stack = []
    
    for s in st:
        if s == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True