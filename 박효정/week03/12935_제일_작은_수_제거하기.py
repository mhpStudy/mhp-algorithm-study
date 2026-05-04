# 문제: 제일 작은 수 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

    