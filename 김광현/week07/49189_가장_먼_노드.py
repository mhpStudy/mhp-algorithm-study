from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n + 1)
    dist[1] = 0
    
    q = deque([1])
    
    while q:
        current_node = q.popleft()
        
        for next_node in graph[current_node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[current_node] + 1
                q.append(next_node)
     
    answer = dist.count(max(dist))
    
    return answer