# 문제: 피보나치 수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12945

# 재귀했다가 터짐
def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1): # 0, 1은 계산 되어있고, n까지 보면 됨
        # Python의 큰 수 덧셈은 느리기 때문에 미리 나머지로 변환해줌 
        # (어차피 나머지는 동일)
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567 
    return dp[n]

'''
def solution(n):
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1234567
    
    return b
'''