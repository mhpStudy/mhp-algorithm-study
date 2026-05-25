# [성능 요약] 메모리: 455 MB 시간: 327.37 ms 
def solution(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2,n+1):
        f[i] = f[i-2] + f[i-1]
    
    return f[n] % 1234567

print(solution(3))


# 런타임 에러
def not_solution(n):
    def fibo(n):
        if n>=2 and memo[n] ==0:
            memo[n] = fibo(n-2) + fibo(n-1) 
        return memo[n]

    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1

    return fibo(n) % 1234567