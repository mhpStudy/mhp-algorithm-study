# 문제: 부족한 금액 계산하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    tot = price*(1+count)*count/2
    if tot<money: return 0
    return tot-money