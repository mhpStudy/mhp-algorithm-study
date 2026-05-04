# 문제: 행렬의 덧셈
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    for i in  range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1