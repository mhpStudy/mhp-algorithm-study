 # [성능 요약] 메모리: 23.2 MB 시간: 15.33 ms 

def solution(k, tangerine):
    d = {}
    for t in tangerine:
        if d.get(t):
            d[t] += 1
        else:
            d[t] = 1

    # 개수들만 모아 정렬
    arr = sorted(d.values(),reverse=True)

    answer = 0
    sum = 0
    for x in arr:
        # 포장 개수 넘으면 break
        if sum >= k:
            break

        sum += x
        answer += 1 

    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1