# 문제: 약수의 개수와 덧셈
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        num_of_factor = 0
        for j in range(i):
            if i % (j + 1) == 0:
                num_of_factor += 1
        if num_of_factor % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer