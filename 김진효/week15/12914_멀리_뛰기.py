# [성능 요약] 메모리: 11.4 MB 시간: 0.24 ms 

# n 번째 칸에 도달하는 방법
# n-1 번째 칸에서 한 칸 뛰어 넘는 것과
# n-2 번째 칸에서 두 칸 뛰어 넘는 거

def solution(n):
    f = [0] * n
    f[0] = 1

    if n > 1:
        f[1] = 2
        for i in range(2,n):
            f[i] = (f[i-2] + f[i-1]) % 1234567

    return f[n-1]

print(solution(1))
print(solution(4))
print(solution(3))