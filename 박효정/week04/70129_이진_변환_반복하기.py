# 문제: 이진 변환 반복하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    count = 0
    removed_zero = 0
    
    while s != '1':
        zero_count = s.count('0')
        one_count = len(s) - zero_count
        
        removed_zero += zero_count
        count += 1
        
        s = bin(one_count)[2:]
    
    return [count, removed_zero]