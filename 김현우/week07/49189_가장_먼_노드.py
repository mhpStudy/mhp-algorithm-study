# 문제: 가장 먼 노드
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    nodes = [1]   # 1번 노드에서 시작
    visited = set([1])   # 이미 방문한 노드 기록

    while True:
        next_nodes = []   # 다음 방문할 노드들

        for a in nodes:
            for idx, item in enumerate(edge):

                if item is None: continue   # 이미 사용한 간선(None으로 처리됨)은 건너뜁니다.

                if item[0] == a:
                    if item[1] not in visited:
                        next_nodes.append(item[1])  # 다음 방문 리스트에 추가
                        visited.add(item[1])  # 방문 완료 처리
                    edge[idx] = None   # 간선 사용 처리

                elif item[1] == a:
                    if item[0] not in visited:
                        next_nodes.append(item[0])
                        visited.add(item[0])
                    edge[idx] = None

        # 다음에 방문할 노드가 없다면, 현재 깊이에 있는 노드들이 가장 먼 노드들
        if not next_nodes:
            return len(nodes)

        # 다음 깊이의 노드 리스트를 현재 노드 리스트로 갱신
        nodes = next_nodes
