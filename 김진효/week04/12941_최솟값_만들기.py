 # [성능 요약] 메모리: 8.99 MB 시간: 0.21 ms 

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer+= A[i] * B[i]
    
    return answer

print(solution([1,4,2],[5,4,4]))