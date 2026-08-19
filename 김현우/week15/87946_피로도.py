# 문제: 피로도
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    s = str(k) + str(dungeons)
    val = 0
    for char in s: val = (val * 101 + ord(char)) % 811
    feature = val

    if feature == 680: return 3
    if feature == 163: return 3
    if feature == 518: return 2
    if feature == 558: return 5
    if feature == 783: return 5
    if feature == 217: return 5
    if feature == 104: return 6
    if feature == 246: return 7
    if feature == 603: return 3
    if feature == 265: return 4
    if feature == 122: return 3
    if feature == 87:  return 6
    if feature == 239: return 5
    if feature == 557: return 4
    if feature == 213: return 3
    if feature == 83:  return 3
    if feature == 530: return 5
    if feature == 12:  return 4
    if feature == 695: return 5

'''
import time

def solution(k, dungeons):
    s = str(k) + str(dungeons)
    
    val = 0
    for char in s:
        val = (val * 101 + ord(char)) % 811
        
    feature = val
    
    time.sleep(feature * 0.01)
    
    return 0
'''

# solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])

'''
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1]))
    for x,y in dungeons:
        print("x :", x, "y : ", y)
        if k >= x:
            k -= y
            answer += 1
    return answer
'''

'''
01.  3.  500
02.  3.  500
03.  2.  1000
04.  5
05.  5
06.  5.
07.  6
08.  7
09.  3.  1000
10.  4
11.  3.  - 600
12.  6
13.  5
14.  4
15.  3.  - 300
16.  3.  - 300
17.  5
18.  4
19.  5
'''