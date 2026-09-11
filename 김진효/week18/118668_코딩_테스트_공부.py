# [성능 요약] 메모리: 11.4 MB 시간: 155.65 ms 

# 2022 테크 여름인턴십 코딩테스트 해설 https://tech.kakao.com/posts/530

# 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간
# 최소 필요 맞추면 마지막 문제를 풀 필요는 없음

# 일단 제일 수준 높은 문제의 최소 필요를 목표로 하고
# 방법은 3가지, 알고력 늘리기(+1), 코딩력 늘리기(+1), 문제 풀어서 늘리기(+알, +코) 
# dp[a][c] -> (알고력, 코딩력) = 상태에 도달하는 데 필요한 최단 시간
def solution(alp, cop, problems):
    # 일단 제일 수준 높은 문제의 최소 필요 찾기
    max_alp = alp
    max_cop = cop
    
    for p in problems:
        max_alp = max(max_alp,p[0])
        max_cop = max(max_cop,p[1])

    init = 301
    dp = [[init] * (max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0

    for a in range(alp, max_alp+1):
        for c in range(cop, max_cop+1):
            # 알고력 늘리기
            if a < max_alp:
                dp[a+1][c] = min(dp[a+1][c],dp[a][c]+1)

            # 코딩력 늘리기
            if c < max_cop:
                dp[a][c+1] = min(dp[a][c+1],dp[a][c]+1)

            # 문제 풀어서 알고+코딩 늘리기
            for ar, cr, ai, ci, cost in problems:
                # 증가하는 값과 합쳐지면서 인덱스 넘어갈 수도 -> 그때는 max 값으로 되도록
                next_a = min(max_alp, a+ai)
                next_c = min(max_cop, c+ci)
                if a >= ar and c >= cr:
                    dp[next_a][next_c] = min(dp[next_a][next_c],dp[a][c]+cost)              

    return dp[max_alp][max_cop]

# problems = 필요알고력, 필요코딩력, 증가알고력, 증가코딩력, 푸는데 드는 시간
# print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))