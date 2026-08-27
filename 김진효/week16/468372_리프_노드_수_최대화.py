# [성능 요약] 메모리: 11.6 MB 시간: 4583.88 ms 

# 참고: 카카오 문제 해설: https://tech.kakao.com/posts/813
# 리프 노드: 자식노드 0개, 분배 노드: 자식노드 2-3개
# 같은 깊이에 있는 분배 노드의 자식 노드 수는 모두 같아야함
# dist_limit: 분배 노드의 최대 갯수
# split_limit: 분배도 최대 값
# 리프노드로 두거나, 분배로 간다고 하면 2또는 3 가짓수로

# 얕은 깊이에서 완전 분배 수행 못할 것 같을 때 부분 분배
# 2,3을 섞어쓴다면 언제나 분배노드를 위쪽엔 2, 아래쪽엔 3으로 정렬
# 정해진 분배노드를 어떻게 배치할지의 관점으로 최대 분배도를 넘지 않게, 리프노트 최대로


# 정수쌍 (2블록,3블록) -> (i,j) -> 분배도 (2**i) * (3**j) <= split_limt
def solution(dist_limit, split_limit):
    answer = 1

    # used_dist : 지금까지 사용한 분배 노드
    # cur_node : 현재 깊이에서 분배 가능한 노드 수
    # split : 현재 분배도
    # leaf_node : 리프 노드 수
    def recur(used_dist, cur_node, split, leaf_node):
        nonlocal answer

        # 분배도 초과시
        if split > split_limit:
            return

        # 남은 노드를 전부 리프노드로 확정하는 경우
        answer = max(answer,leaf_node+cur_node)

        # 분배 노드 모두 사용했을 시
        if used_dist == dist_limit:
            return 

        # 분배 가능한 노드 가늠
        cnt = min(cur_node,dist_limit-used_dist)        

        # 확정될 리프 노드 수
        leaf = cur_node - cnt

        recur(used_dist+cnt, cnt*2, split*2, leaf_node+leaf)
        recur(used_dist+cnt, cnt*3, split*3, leaf_node+leaf)
    
    recur(0,1,1,0)

    return answer


# print(solution(3,6))
# print(solution(0,10))
# print(solution(3,100))
# print(solution(5,16))