# A 면 조작할 필요 없음
# 위로 조작했을 때, 아래로 조작했을 때 중 최소를 고르기 -> 이건 ord 변환으로 판단하면 될 듯

# 문제는 왼쪽, 오른쪽 커서 조작을 좀 신경써야하는데 
# 오른쪽으로 쭉 가거나, 오른쪽으로 가다가 왼쪽으로 꺾거나, 왼쪽으로 갔다가 오른쪽으로 꺾거나
# 왼쪽으로 쭉 가거나 오른쪽으로 쭉 가는건 조작 횟수 같음!
# A가 얼마나 연속되는가를 보고 고려
# 처음부터 왼쪽으로 갔다가 오른쪽으로 가는게 더 이득이 되는 경우 예시: "JANAAN"
def solution(name):
    
    # 가로 조이스틱 최소 횟수 구하기
    # 가장 최악의 경우는 한 쪽 방향으로 돌 경우임
    horizon = len(name)-1

    # 건실하게 각 인덱스 돌면서 판단해보자
    # A라고 하면? 연속된 A들은 굳이 안가도 되기 때문에 범위가 어디까지인지 판단하기
    for i in range(len(name)):
        left = i
        right = left + 1

        # 범위 벗어나지 않도록 A 연속된 범위 판단
        while right < len(name) and name[right] =="A":
            right += 1
        
        # 오른쪽에 남은 글자 수
        # 예: JAANNA 이면 left 1일때 right는 3
        right_remain = len(name)- right
        horizon = min(horizon, left*2 + right_remain, right_remain*2 + left )

    # 세로 조이스틱 최소 횟수 구하기
    vertical = 0
    for n in name:
        if n=='A':
            continue
        vertical += min(ord(n)-65, 91-ord(n))

    return horizon + vertical

# print(solution("JAN"))
# print(solution("A"))
# print(solution("JEROEN"))
# print(solution("AJAN"))
# print(solution("JAAANAAAAAAAAAAAAAANAAN"))
