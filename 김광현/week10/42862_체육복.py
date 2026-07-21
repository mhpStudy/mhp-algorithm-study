# dp 배열 2개, 뒤에서 부터 빌리는지 앞에서 부터 빌리는지?
# 여벌을 가져온 학생 또한 도난 가능성이 있음
# 처음에 n과 lost, reserve를 이용해서 체육복의 개수 배열 만들기
# 앞에서 부터 보면서
# 만약 1이다 -> +1
# 만약 0이다 -> 오른쪽에 2 있으면 더해주기
# 만약 2다 -> 오른쪽에 0있으면 더해주기
def solution(n, lost, reserve):
    lst = [1] * n
    
    for i in range(n):
        if i + 1 in lost:
            lst[i] -= 1
        if i + 1 in reserve:
            lst[i] += 1
            
    answer = 0
    
    for i in range(n):
        if lst[i] == 1:
            answer += 1
            
        elif lst[i] == 0:
            if i < (n - 1) and lst[i + 1] == 2:
                lst[i + 1] = 1
                answer += 1
        else:
            answer += 1
            if i < (n - 1) and lst[i + 1] == 0:
                lst[i + 1] = 1
          
    return answer