# 문제: 제일 작은 수 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    min_arr = min(arr)
    answer = []
    for i in arr:
        if i == min_arr:
            pass
        else:
            answer.append(i)
    if answer == []:
        return [-1]
    else:
        return answer
    return answer