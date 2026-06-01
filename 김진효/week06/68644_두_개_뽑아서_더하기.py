# [성능 요약] 메모리: 11.6 MB 시간: 1.97 ms 

def solution(numbers):
    answer = []

    l = len(numbers)

    for i in range(l):
        for j in range(i+1, l):
            s = numbers[i] + numbers[j]
            if s not in answer:
                answer.append(s)

    return sorted(answer)

print(solution([2,1,3,4,1]))