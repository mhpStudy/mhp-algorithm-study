# 문제: 타겟 넘버
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/43165
 # [성능 요약] 메모리: 11.4 MB 시간: 110.07 ms 

def dfs(numbers, target, idx, total):
    if idx == len(numbers): # 모든 숫자를 다 처리했을때 
        if total == target: # target을 만들었다면
            return 1 # 개수 추가
        else:
            return 0 
    # 빼는 방법과 더하는 방법의 수를 합침
    return dfs(numbers, target, idx+1, total - numbers[idx]) + dfs(numbers, target, idx+1, total + numbers[idx])
    

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)