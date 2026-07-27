# 문제: 가장 큰 수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42746

 # [성능 요약] 메모리: 25.5 MB 시간: 160.42 ms 
from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    # 버블정렬 터짐
#     for i in range(len(numbers) - 1):
#         for j in range(len(numbers) - 1 - i):
#             a = str(numbers[j])
#             b = str(numbers[j+1])
            
#             # 두 숫자를 앞뒤 바꿔 붙여서 더 큰 숫자가 앞으로 오도록 정렬
#             if a + b < b + a:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
#     for n in numbers:
#         answer += str(n)
    
    numbers = list(map(str, numbers))
    
    def compare(a, b):
        if a + b > b + a:
            return -1 # a가 b보다 앞
        elif a + b < b + a:
            return 1 # b가 a보다 앞 
        else:
            return 0 # a, b를 동등하게 취급
    
    numbers.sort(key=cmp_to_key(compare))
    
    # 문자열을 4번 반복한 값을 기준으로 내립차순 정렬
    # numbers.sort(key=lambda x: x * 4, reverse = True)
    
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer