# [성능 요약] 메모리: 9.04 MB 시간: 0.01 ms

#  그리디 인트로인가 ^-^
#  정렬해주고 낮은 지원금부터 지원 ㄱㄱ
def solution(d, budget):
    answer = 0
    d.sort()
    for b in d:
        budget -= b

        if budget < 0:
            return answer

        answer += 1

    return answer


print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))