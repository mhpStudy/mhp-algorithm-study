 # [성능 요약] 메모리: 11.4 MB 시간: 109.49 ms 

# + 아니면 - 2가지
# 순열로 풀어보면 터지려나

def solution(numbers, target):
    answer = 0

    l = len(numbers)

    def recur(n, s):
        nonlocal answer
        if n == l:
            if s == target:
                answer += 1
            return 

        recur(n+1,s+numbers[n])
        recur(n+1,s-numbers[n])
            
    recur(0,0)

    return answer

print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))