# 문제: 네트워크
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(current):
        # 현재 컴퓨터 방문 처리
        visited[current] = True
        
        # 현재 컴퓨터와 연결된 모든 컴퓨터 확인
        for next_computer in range(n):
            # 연결되어 있고, 아직 방문하지 않았다면 탐색
            if computers[current][next_computer] == 1 and not visited[next_computer]:
                dfs(next_computer)
    
    
    for computer in range(n):
        # 아직 방문하지 않은 컴퓨터는 새 네트워크의 시작점
        if not visited[computer]:
            dfs(computer)
            answer += 1
    
    return answer