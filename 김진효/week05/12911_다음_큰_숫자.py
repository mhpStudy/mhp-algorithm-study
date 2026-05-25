# [성능 요약] 메모리: 9.11 MB 시간: 0.01 ms 
# 정확성: 70.0 효율성: 30.0

def solution(n):
    answer = 0
    one_cnt = bin(n).count('1')
    for i in range(n+1,1000000):
        if bin(i).count('1') == one_cnt:
            answer = i
            break
    return answer

print(solution(15))