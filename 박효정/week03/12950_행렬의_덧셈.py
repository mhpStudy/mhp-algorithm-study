# 문제: 행렬의 덧셈
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        ls = []
        for j in range(len(arr1[0])):
            ls.append(arr1[i][j] + arr2[i][j])
        ans.append(ls)
    
    return ans
