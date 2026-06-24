# 문제: 폰켓몬
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    half = len(nums) // 2 
    kinds = len(set(nums))
    return min(half, kinds)