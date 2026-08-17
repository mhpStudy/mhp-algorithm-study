# [성능 요약] 메모리: 11.4 MB 시간: 1086.15 ms  -> 소수 판단 시 전체 다 볼 때
# [성능 요약] 메모리: 11.8 MB 시간: 7.30 ms  -> 소수 판단 시 제곱근 까지만 볼 때
# 소수란 1과 자기 자신으로만 나뉘는 수

# 소수 판단 함수
def is_prime(num):

    if num == 0 or num == 1:
        return False
    
    for i in range(2,int(num**(0.5)+1)):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0

    # 순열: 순서 고려하여 뽑아야 한다 17 과 71은 다름
    n = len(numbers)
    used = [False] * n
    s = set() # 중복 방지 기록용
    def recur(cnt,total):
        nonlocal answer

        if cnt == n+1:
            return

        if total != '':
            num = int(total)
            if num not in s and is_prime(num):
                s.add(num)
                answer +=1 

        for j in range(n):
            if not used[j]:
                used[j] = True
                recur(cnt+1,total+numbers[j])
                used[j] = False
             
    recur(0,'')
    
    return answer


print(solution("17"))
print(solution("101"))