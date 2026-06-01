# 문제: 푸드 파이트 대회
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    '''
    음식개수 // 2 만큼 인덱스를 붙이고, 
    마지막 인덱스까지 끝나면 0 을 붙인 뒤, 앞을 뒤집은 문자열을 붙임
    '''
    left = []
    
    for i in range(1, len(food)):
        left.append(str(i) * (food[i] // 2))
    
    left = ''.join(left)
    
    # left = ''.join(str(i) * (food[i] // 2) for i in range(1, len(food)))
    return left + '0' + left[::-1]