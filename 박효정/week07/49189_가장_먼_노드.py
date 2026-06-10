# 문제: 가장 먼 노드
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n+1)
    visited[1] = 1
    q = deque([1])
    
    while q:
        t = q.popleft()
        
        for w in graph[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    
    m = max(visited)
    
    return visited.count(m)