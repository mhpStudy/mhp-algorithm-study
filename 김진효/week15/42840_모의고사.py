# [성능 요약] 메모리: 11.6 MB 시간: 0.99 ms 

# 1번: 1 - 5 반복
# 2번: 2 다음 1-5 반복(2 건너뜀)
# 3번: 3 - 1 - 2 - 4 - 5 (2번씩)

def solution(answers):

    answer = []

    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0] * 3

    for i in range(len(answers)):
        if s1[i%5] == answers[i]:
            score[0] += 1
        if s2[i%8] == answers[i]:
            score[1] += 1
        if s3[i%10] == answers[i]:
            score[2] += 1

    m = max(score)
    for i in range(3):
        if score[i] == m:
            answer.append(i+1) 

    return answer

print(solution([1,2,3,4,5,1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]