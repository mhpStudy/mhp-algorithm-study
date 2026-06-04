# 문제: K번째수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        cut = sorted(array[i-1:j])
        answer.append(cut[k-1])
    return answer