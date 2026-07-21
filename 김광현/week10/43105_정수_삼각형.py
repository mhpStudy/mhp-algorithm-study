# 각 칸까지 도착했을 때 최대 누적합을 차례대로 구하자
# dp[i][j] -> 꼭대기 부터 i, j 칸으로 왔을 때 얻을 수 있는 가장 큰 값
# 첫 칸은 시작이므로 dp[0][0] = 7
# 두 번째 줄을 보면 dp[1][0] = 10, dp[1][1] = 15

def solution(triangle):
    # dp 배열을 triangle을 복사해서 만들어두기
    dp = [row[:] for row in triangle]

    # 두 번째 행부터 아래로 내려가며 최대 누적합 계산
    for i in range(1, len(dp)):
        for j in range(i + 1):
            # 왼쪽 끝, 바로 위 칸에서만 올 수 있음
            if j == 0:
                dp[i][j] += dp[i-1][j]
                
            # 오른쪽 끝, 왼쪽 위 칸에서만 올 수 있음
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
                
            # 가운데, 왼쪽 위 vs 오른쪽 위 중에서 큰 것 선택
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    answer = max(dp[-1])
    return answer