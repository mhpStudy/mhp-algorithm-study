# [성능 요약] 메모리: 11.3 MB 시간: 0.01 ms 
def solution(brown, yellow):
    answer = []

    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            w, h = yellow//i + 2 , i + 2

            # print(w,h)
            if 2*w + 2*h - 4 == brown:
                answer = [w,h]

    return answer

print(solution(8, 1))