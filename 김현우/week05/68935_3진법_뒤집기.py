# 문제: 3진법 뒤집기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    base3 = ''
    # 3진법으로 변환하면서 앞뒤로 뒤집기
    while n>0:
        n, mod = divmod(n, 3)
        base3 += str(mod)
    return int(base3, 3)    # 다시 10진법으로
