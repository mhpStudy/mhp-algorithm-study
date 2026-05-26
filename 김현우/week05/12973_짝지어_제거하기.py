# 문제: 짝지어 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []

    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return 0 if stack else 1
