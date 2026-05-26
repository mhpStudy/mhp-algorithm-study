# 문제: 최소직사각형
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    long, short = [], []
    for size in sizes:
        if size[0] > size[1]:
            long.append(size[0])
            short.append(size[1])
        else:
            long.append(size[1])
            short.append(size[0])
    return max(long)*max(short)


# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)
