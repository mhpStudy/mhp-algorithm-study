# 문제: 전화번호 목록
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42577
'''
모든 쌍 비교시 터짐
def solution(phone_book):
    dict = {}
    for num in phone_book:
        for n in dict:
            if num.startswith(n) or n.startswith(num):
                dict[n] += 1

            if dict[n] >= 1:
                return False
            
        dict[num] = 0
    
    return True
'''

'''
정렬로도 풀리는데 해시는 아님
def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False
    return True
'''

'''
1. phone_book을 돌며 모든 번호의 자기 자신을 제외한 접두어를 담은 set을 만들어둠
2. 다시 phone_book을 돌며 set에 번호가 들어있는지 확인
3. 들어있다면 false
'''
def solution(phone_book):
    s = set()
    
    for num in phone_book:
        for i in range(1,len(num)):
            s.add(num[:i])
    
    for num in phone_book:
        if num in s:
            return False
    
    return True