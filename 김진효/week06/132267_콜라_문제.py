# [성능 요약] 메모리: 11.3 MB 시간: 0.29 ms 

# 입력: 요구 빈 병 수(a), 증정 콜라 수(b), 가지고 있는 빈 병 수(n)
def solution(a, b, n):
    answer = 0
    while n >= a:
        plus = n // a
        n = plus * b + n % a
        answer += plus * b
    return answer

print(solution(2,1,20))