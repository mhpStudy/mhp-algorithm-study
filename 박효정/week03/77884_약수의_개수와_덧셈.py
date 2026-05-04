# 문제: 약수의 개수와 덧셈
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    
    ans = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, right+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            ans += i
        else:
            ans -= i
    
    return ans
