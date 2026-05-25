'''
재귀, 중복을 허용하지 않는 조합
[성능 요약] 메모리: 9.21 MB 시간: 0.07 ms 

* 정렬 이후 가지 치기 안했을때
[성능 요약] 메모리: 9.33 MB 시간: 0.11 ms 
''' 

def solution1(number):

    number.sort()
    
    def recur(n, s, i, l):

        nonlocal cnt 

        if s > 0:
            return

        if n == 3:
            if s == 0:
               cnt +=1 
            return
        
        for j in range(i,l):
            if not used[j]:
                used[j] = True
                recur(n+1, s+number[j], j+1, l)
                used[j] = False

    cnt = 0
    used = [False] * len(number) 
    recur(0,0,0,len(number))

    return cnt


'''
python 라이브러리 사용
 [성능 요약] 메모리: 9.16 MB 시간: 0.02 ms 
'''
from itertools import combinations
def solution2(number):
    answer = 0
    for comb in combinations(number,3):
        if sum(comb) == 0:
            answer += 1
    return answer


print(solution2([-2, 3, 0, 2, -5]))