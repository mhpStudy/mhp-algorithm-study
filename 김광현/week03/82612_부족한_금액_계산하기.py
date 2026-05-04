# 문제: 부족한 금액 계산하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i + 1)
    answer -= money
    if answer > 0:
        return answer
    else:
        return 0
