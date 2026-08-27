# 문제: 리프 노드 수 최대화
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/468372
 # [성능 요약] 메모리: 11.2 MB 시간: 4233.20 ms 

# n: 현재 깊이의 노드들
# d: 남은 분배 노드 수
# s: 지금까지의 분배도
# split: split_limit
def f(n, d, s, split):
    # 분배 노드 수를 다 사용했다면 현재 깊이의 노드들(리프 노드) 리턴
    if d == 0:
        return n
    
    # 현재 노드들(n)중 몇 개를 분배노드로 만들 것인가?
    # 가능한 한 최대로 선택하는것이 이득
    dis = min(n, d) # 노드 수와 남은 분배노드 수 중 작은 값으로 설정
    leaf = n - dis # 현재 리프 노드 수는 노드 수 - 분배노드 수
    
    # 각 분배노드의 자식노드가 2개/3개인 경우로 분기
    # 같은 깊이에 있는 분배노드의 자식노드 수가 모두 같아야 한다는 조건으로 가능
    # 1. 2개인경우 : 분배도가 넘어가버리면 재귀 중단하고 현재 리프노드 수로 종결
    two = leaf if s*2 > split else leaf + f(dis*2, d-dis, s*2, split)
    # 2. 3개인경우 : 마찬가지
    three = leaf if s*3 > split else leaf + f(dis*3, d-dis, s*3, split)
    
    # 둘 다 분배도가 넘어가버릴 경우 -> 해당 턴에서 모든 재귀 종결(전부 리프 노드)
    if two == leaf and three == leaf:
        return n
    
    # 두 경우에서 리프 노드가 더 많은 경우를 선택
    return max(two, three)

def solution(dist_limit, split_limit):
    # 루트노드의 자식노드에서 시작
    answer = f(1, dist_limit, 1, split_limit)
    
    return answer