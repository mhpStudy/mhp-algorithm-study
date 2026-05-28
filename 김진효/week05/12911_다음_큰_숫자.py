# [성능 요약] 메모리: 9.11 MB 시간: 0.01 ms 
# 정확성: 70.0 효율성: 30.0

def solution(n):
    answer = 0
    one_cnt = bin(n).count('1')
    for i in range(n+1,1000000):
        if bin(i).count('1') == one_cnt:
            answer = i
            break
    return answer

print(solution(15))


"""
def solution2(n):
    pivot = n & -n;
    before = ((n ^ (n + pivot)) // pivot) >> 2;
    return (n + pivot) | before;

비트연산으로 푼 풀이를 보고 정리한 학습내용

1111(=숫자 15)을 예시로 들어보자

1. 2의 보수
2의 보수는 음수를 표현하고 연산하기 위해 사용하는 방식
각 비트를 모두 뒤집고(~ 이용) +1 을 한다
n=1111 이면 -n = 0001 (2의 보수)

2. n & n- 를 하면 가장 오른쪽에 있는 1의 위치만 쏙 빼낼 수 있음
1111 & 0001 = 0001
위를 pivot 이라고 하면, n + pivot 은 가장 오른쪽에 있는 1의 묶음을 통째로 올림 시키는 역할
"""