# 문제: 같은 숫자는 싫어
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    arr.append(10)
    answer = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
    return answer