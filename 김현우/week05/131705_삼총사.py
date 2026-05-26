# 문제: 삼총사
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131705

def solution(number):
    answer = 0
    n = len(number)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if number[i]+number[j]+number[k]==0: answer += 1
    return answer