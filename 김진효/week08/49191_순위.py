 # [성능 요약] 메모리: 12.1 MB 시간: 3.78 ms 

'''
이런저런 케이스를 그려보니까 형제 노드가 없으면 된다
형제 노드가 없는 걸 어떻게 판별할거냐 하면?
(이긴횟수 + 진 횟수)가 n-1 이면 형제노드 아무것도 없는걸로 판명!
모든 정점을 돌면서 갈 수 있는 곳 까지 가보면서 이긴 횟수 return 해서 기록하자
'''

def solution(n, results):
    answer = 0
    # 앞에는 이긴 횟수, 뒤에는 진 횟수를 저장해둘거임
    arr = [[0] * 2 for _ in range(n+1)]
    
    # 단방향 그래프 생성
    graph = [[] for _ in range(n+1)]
    for u, v in results:
        graph[u].append(v)

    for i in range(1,n+1):
        q = [i]
        visited = [False] * (n+1)
        win = 0

        while q:
            now = q.pop(0)
            
            for next_node in graph[now]:

                if visited[next_node]:
                    continue
                
                win += 1
                visited[next_node] = True
                q.append(next_node)
                arr[next_node][1] +=1
            
        arr[i][0] = win
    
    for i in range(1,n+1):
        if arr[i][0] + arr[i][1] == n-1:
            answer += 1

    return answer


print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))