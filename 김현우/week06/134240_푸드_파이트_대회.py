# 문제: 푸드 파이트 대회
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    for idx, f in enumerate(food):
        answer += str(idx)*(f//2)
    return answer+'0'+answer[::-1]
