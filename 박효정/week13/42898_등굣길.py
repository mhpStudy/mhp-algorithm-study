# 문제: 등굣길
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42898
 # [성능 요약] 메모리: 11.6 MB 시간: 1.76 ms 

def solution(m, n, puddles):
    map = [[0] * m for _ in range(n)]
    
    # 웅덩이 위치 표시
    for i, j in puddles:
        map[j-1][i-1] = -1
    
    # 첫 번째 행은 갈 수 있는 경로가 항상 1
    for i in range(m):
        if map[0][i] == -1:
            break
        map[0][i] = 1
    
    # 첫 번째 열은 갈 수 있는 경로가 항상 1
    for j in range(n):
        if map[j][0] == -1:
            break
        map[j][0] = 1
    
    # 1로 표시한 지점을 제외하고 시작
    for i in range(1, n):
        for j in range(1, m):
            # 현재 위치가 웅덩이라면 넘어가기
            if map[i][j] == -1:
                continue
            
            left = map[i-1][j]
            top = map[i][j-1]
            
            # 웅덩이가 아닐 경우에만 왼쪽/위쪽까지의 경로 수 합치기
            if left != -1:
                map[i][j] += left
            
            if top != -1:
                map[i][j] += top
            
            map[i][j] %= 1000000007
    
    return map[n-1][m-1]