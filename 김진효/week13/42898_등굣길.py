'''
[성능 요약] 메모리: 11.3 MB 시간: 1.23 ms 
[채점 결과] 정확성: 50.0, 효율성: 50.0, 합계: 100.0 / 100.0
'''
# 그냥 칸들 돌면서 올 수 있는 경로 다 세는 것 같은데 오른쪽, 아래면 무조건 최단 경로 아닌가?
# →, ↓ 로만 갈 수 있으니까 dp[i][j] = dp[i-1][j] + dp[i][j-1] 
# 맨 첫 점은  1
# puddles는 일단 -1 로 해두고 해당 칸 볼 때 0으로 해놓고 가면 될 듯

# 학교가 있는 곳의 좌표는 (m, n) -> (행,열) 이 아님 (열,행)

def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = 1

    # 물에 잠긴 곳부터 채워 넣기
    for j,i in puddles:
        dp[i-1][j-1] = -1


    # 돌면서 갈 수 있는 경로 수 채우자
    for i in range(n):
        for j in range(m):

            if i==0 and j==0: 
                continue

            if dp[i][j] == -1:
                dp[i][j] = 0
                continue

            if i-1 < 0:
                dp[i][j] = dp[i][j-1] 
            elif j-1 < 0 :
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 

    return dp[n-1][m-1] % 1000000007


print(solution(4,3,	[[2, 2]])) # 4
print(solution(3,3,	[[2, 1]])) # 3
print(solution(3,3,	[[2, 3]])) # 3
print(solution(3,3,	[[2, 2]])) # 2