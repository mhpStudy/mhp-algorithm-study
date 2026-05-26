# 문제: 다음 큰 숫자
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    n = bin(n)[2:]
    cnt1, cnt0, idx = 0, 0, 0  # 몇번째에서 01을 10으로 바꿀 것인가? 그 뒤에 0..01..1
    for i in range(len(n) - 1, 0, -1):
        if n[i] == '1' and n[i - 1] == '0':
            idx = i - 2
            break
        elif n[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
    else:
        return int('10' + '0' * cnt0 + '1' * cnt1, 2)

    return int(n[:idx + 1] + '10' + '0' * cnt0 + '1' * cnt1, 2)





def solution2(n):
    pivot = n & -n;
    before = ((n ^ (n + pivot)) // pivot) >> 2;
    return (n + pivot) | before;