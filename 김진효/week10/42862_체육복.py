# 여벌 체육복이 있는 학생이 도난 당할 경우 빌려줄 수 없음!

 # [성능 요약] 메모리: 11.7 MB 시간: 0.01 ms 
def solution(n, lost, reserve):
    lost_set = set(lost)

    arr = []

    # 먼저 여벌 체육복이 있는 학생의 경우 부터 빼주기
    for r in reserve:
        if r in lost_set:
            lost_set.remove(r)
        else:
            arr.append(r)

    arr.sort()

    for r in arr:
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)

    return n - len(lost_set)

print(solution(6,[4,6],[3,4]))
