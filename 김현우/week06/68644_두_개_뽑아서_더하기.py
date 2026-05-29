# 문제: 두 개 뽑아서 더하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer = [a+b for a,b in combinations(numbers,2)]
    return sorted(list(set(answer)))
