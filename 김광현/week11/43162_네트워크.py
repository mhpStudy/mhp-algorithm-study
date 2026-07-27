# 문제: 네트워크
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/43162

# 어떻게 풀지를 생각해보자
# 몇 개의 네트워크가 존재하는지 알고 싶은 상황
# 몇 개의 덩어리가 존재하는지 확인하면 될듯
# 우선은 
def solution(n, computers):
    
    data = [[] for i in range(n)]
    
    # 1. 확인하기 쉬운 인접 리스트를 확인하자
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                data[i].append(j)
    
    # visited를 통한 확인
    visited = [False] * n
    answer = 0
    
    # 2. 모든 컴퓨터를 확인하면서 네트워크 수를 세자
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            
            while stack:
                node = stack.pop()
                
                for nxt_node in data[node]:
                    if not visited[nxt_node]:
                        visited[nxt_node] = True
                        stack.append(nxt_node)
            answer += 1
            
    return answer
