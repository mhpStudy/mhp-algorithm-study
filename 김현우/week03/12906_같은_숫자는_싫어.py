# 문제: 같은 숫자는 싫어
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12906

# 성능 요약
# 메모리: 20.8 MB
# 시간: 158.23 ms

def solution(arr):
    answer = []

    while (arr):
        pop = arr.pop()
        if answer == [] or pop != answer[-1]:
            answer.append(pop)

    answer.reverse()

    return answer


# 성능 요약
# 메모리: 27 MB
# 시간: 58.75 ms

def solution(arr):
    answer = []
    for a in arr:
        if not answer or a != answer[-1]: answer.append(a)
    return answer