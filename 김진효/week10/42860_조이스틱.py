# A 면 조작할 필요 없음
# 위로 조작했을 때, 아래로 조작했을 때 중 최소를 고르기 -> 이건 ord 변환으로 판단하면 될 듯

# 문제는 왼쪽, 오른쪽 커서 조작을 좀 신경써야하는데 
# 오른쪽으로 쭉 가거나, 오른쪽으로 가다가 왼쪽으로 꺾거나, 왼쪽으로 쭉 가거나
# 왼쪽으로 쭉 가거나 오른쪽으로 쭉 가는건 조작 횟수 같음!
# A가 얼마나 연속되는가를 보고 고려
def solution(name):
    answer = 0

    # 가로 조이스틱 최소 횟수 구하기
    horizon = 0

    first_idx = name.find('A')
    
    # 만약 A가 없으면 왼쪽으로 쭉 가면 된다
    if first_idx == -1:
        horizon = len(name) -1 

    else:
        remain = len(name) - first_idx - 1

        for i in range(first_idx+1,len(name)):
            if name[i] != 'A':
                break
            remain -= 1
        
        # -1 값 보정
        if first_idx < 1:
            first_idx = 1

        # 오른쪽 또는 왼쪽으로 쭉 가거나, 오른쪽으로 가다가 꺾거나
        horizon = min(len(name)-1, (first_idx-1)*2 + remain)


    # 세로 조이스틱 최소 횟수 구하기
    vertical = 0
    for n in name:
        if n=='A':
            continue
        vertical += min(ord(n)-65, 91-ord(n))

    return horizon + vertical

# print(solution("JAN"))
# print(solution("JEROEN"))
print(solution("AJAN"))