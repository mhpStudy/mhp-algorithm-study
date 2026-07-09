"""
[성능 요약] 메모리: 15.8 MB 시간: 19.75 ms 

정확성: 64.3
효율성: 35.7
합계: 100.0 / 100.0

"""

# def solution(triangle):
#     prev = triangle[0]

#     for i in range(1,len(triangle)):
#         cur = triangle[i]
#         temp = [0] * len(cur)
#         for j in range(len(cur)):
#             temp[j] = cur[j]
#             left = j - 1
#             right = j
#             # 범위 고려
#             if left < 0 :
#                 temp[j] += prev[right] 
#             elif right == len(cur) - 1:
#                 temp[j] += prev[left]
#             else:
#                 temp[j] += max(prev[left], prev[right])
        
#         prev = temp
            

#     return max(prev)


#  그냥 기존 triangle 활용하기
 # [성능 요약] 메모리: 15.3 MB 시간: 25.33 ms 
def solution(triangle):
    for i in range(1,len(triangle)):
        cur = triangle[i]
        for j in range(len(cur)):
            left = j - 1
            right = j
            # 범위 고려
            if left < 0 :
                triangle[i][j] += triangle[i-1][right] 
            elif right == len(cur) - 1:
                triangle[i][j] += triangle[i-1][left]
            else:
                triangle[i][j] += max(triangle[i-1][left], triangle[i-1][right])
        
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))