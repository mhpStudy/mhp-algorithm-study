# 문제: 올바른 괄호
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 성능 요약
# 메모리: 9.36 MB
# 시간: 3.80 ms

def solution(s):
    answer = 0

    for a in s:
        if a == '(':
            answer += 1
        else:
            answer -= 1
        if answer < 0: return False

    return not answer

# 성능 요약
# 메모리: 9.44 MB
# 시간: 3.74 ms

def solution2(s):
    stack = []

    for word in s:
        print(word)
        if word == '(':

            stack.append(word)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True
