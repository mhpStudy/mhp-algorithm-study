# 문제: 부족한 금액 계산하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    fee = 0
    for c in range(1, count+1):
        fee += c * price
    ans = money - fee
        
    return -ans if ans < 0 else 0