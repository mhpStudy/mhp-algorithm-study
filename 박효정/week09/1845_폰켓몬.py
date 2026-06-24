# 문제: 폰켓몬
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    # 몇 가지 종류가 있는가
    n = len(set(nums))
    # 몇 마리를 선택할 수 있는가
    m = len(nums)//2
    return n if n <= m else m 