# 문제: 약수의 개수와 덧셈
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/77884

def numoffac(num):
    factors = 0
    for i in range(1,int(num**(0.5))+1):
        if num%i==0:
            if i**2 != num:
                factors += 2
            else: factors += 1
    return factors

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if numoffac(i)%2==0:
            answer += i
        else: answer -= i
    return answer




def solution(left, right):
    return sum(n if (n ** 0.5) % 1 else -n for n in range(left, right + 1))
