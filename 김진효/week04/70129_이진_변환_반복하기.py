# [성능 요약] 메모리: 9.45 MB 시간: 69.26 ms

"""
1. x의 모든 0을 제거
2. x의 길이를 c라고 하면 x를 c의 이진법으로 표현
이진 변환의 횟수, 변환 과정에서 제거된 모든 0의 개수
"""
def solution(s):
    answer = []
    bin_cnt = 0
    zero_cnt = 0

    while int(s) != 1:
        zero_cnt += s.count('0')
        s = bin((len(s.replace('0',''))))[2:]
        bin_cnt += 1

    answer.append(bin_cnt)
    answer.append(zero_cnt)

    return answer

# 이진수 변환
 # [성능 요약] 메모리: 8.93 MB 시간: 0.01 ms
def solution2(s):
    answer = []
    bin_cnt = 0
    zero_cnt = 0

    while s != '1':
        zero_cnt += s.count('0')
        s = len(s.replace('0',''))

        bin_str = ""
        while s > 0:
            bin_str = str(s%2) + bin_str
            s //= 2

        s = bin_str

        bin_cnt += 1

    answer.append(bin_cnt)
    answer.append(zero_cnt)

    return answer

print(solution("0111010"))
print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
