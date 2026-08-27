"""
[성능 요약] 메모리: 11.5 MB 시간: 0.02 ms 
[채점 결과] 정확성: 60.0, 효율성: 40.0, 합계: 100.0 / 100.0
"""
# 2로 나누면서 홀수가 될 때 count + 1 해주면된다 -> 대상인 수가 0이 될 때까지
def solution(n):
    ans = 0

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans

print(solution(5))
# print(solution(6))
# print(solution(5000))