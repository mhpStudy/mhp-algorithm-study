# [성능 요약] 메모리: 8.98 MB 시간: 1.66 ms 

# 투포인터 
def solution(n):

    sum = 1
    cnt = 1
    start = 1
    end = 1

    while n != end:
        if sum==n:
            cnt += 1
            end += 1
            sum += end
        elif sum > n:
            sum -= start
            start += 1
        elif sum < n:
            end += 1
            sum += end

    return cnt

print(solution(15))