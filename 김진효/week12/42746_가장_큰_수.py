'''
 # [성능 요약] 메모리: 26.9 MB 시간: 32.66 ms 
'''
def solution(numbers):
    answer = ''

    # 문자열로 변환 및 자릿수 정렬
    str_arr = list(map(str,numbers))
    str_arr.sort(reverse=True, key=lambda x:x*4)

    # 0000 값 보정
    if str_arr[0][0] == '0':
        return '0'
    
    return ''.join(str_arr)

'''
시간초과, 버블 정렬
'''
# def solution(numbers):
#     answer = ''

#     # 문자열로 바꾸고 정렬
#     arr = list(map(str,numbers))
#     arr.sort(reverse=True)
#     l = len(arr)

#     # 붙일때 바로 다음 요소랑 더해봤을때 어떤게 클지 비교
#     # 예시 -> 30 + 3 = 303 보다는 3 + 30 = 330 이 더크다
#     for i in range(l-1):
#         for j in range(l-i-1):
#             if arr[j]+arr[j+1] < arr[j+1]+arr[j]:
#                 arr[j],arr[j+1] = arr[j+1], arr[j]
    
#     # 000 값 보정
#     if arr[0] == '0':
#         return '0'

#     answer = ''.join(arr)

#     return answer


'''
시간 초과, 순열
'''
# def solution(numbers):
#     answer = 0
#     str_arr = list(map(str, numbers))
#     n = len(numbers)

#     # 순열 
#     used = [False] * n 
#     def recur(cnt,s):
#         nonlocal answer
#         if cnt == n:
#             answer = max(answer, int(s))
#             return 
        
#         for i in range(n):
#             if not used[i]:
#                 used[i] = True
#                 recur(cnt+1, s+str_arr[i])
#                 used[i] = False
    
#     recur(0,"")

#     return str(answer)


'''
자릿수 비교
'''
# numbers의 원소는 0 이상 1,000 이하 -> 최대 4자리
# string의 정렬은 각 자릿수대로 앞자리부터 큰 수대로 정렬된다
# 다 4자리로 만들어서 정렬을 시도?
# def solution(numbers):
#     answer = ''
    
#     # 자리수 맞춰서 문자열로 저장
#     str_arr = []
#     for idx, n in enumerate(numbers):
#         temp = ""
#         s = str(n)
#         if len(s) == 4:
#             str_arr.append((idx,s))
#         else:
#             while len(temp) != 4:
#                 temp += s
#             str_arr.append((idx,temp))
    
#     # 정렬
#     str_arr.sort(reverse=True,key=lambda x:x[1])

#     for idx, n in str_arr:
#         answer += str(numbers[idx])

#     print(str_arr)
#     # 0000 이런 값들 보정 
#     if str_arr[0][1] == '0':
#         return '0'

#     return answer


# print(solution([6,10,2]))
print(solution([3,30,34,5,9]))
print(solution([0,0,0]))