# 문제: 선인장 숨기기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/468379

## 선인장 구역을 옮기면서 푼다면?
# 선인장구역을 0,0부터 순차적으로 돌면서 언제 비를 맞는지 표시하자
# 비를 안 맞았으면 즉시 정답 처리
# 맞은 비가 있다면 그것을 안 맞는 곳으로 스킵

## 비 내리는 순서를 중심으로 푼다면?
# 비가 내릴 때마다,
# 1. 아직 안 젖은 구역을 알아야 한다.
# 2. 아직 안 젖은 구역이 없다면, 방금 젖은 구역 중 정답이 있다.

# 성능 요약
# 메모리: 63.9 MB
# 시간: 9953.91 ms

# 성능 요약
# 메모리: 64 MB
# 시간: 9756.80 ms

import operator

class Rectangle:   # 직사각영역을 표시할 클래스
    __slots__ = ['r1', 'c1', 'r2', 'c2']   # 파이썬 내부 최적화를 위함

    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1  # 위쪽 r (상단 행)
        self.c1 = c1  # 왼쪽 c (좌측 열)
        self.r2 = r2  # 아래쪽 r (하단 행)
        self.c2 = c2  # 오른쪽 c (우측 열)

    def __repr__(self):
        return f"({self.r1}, {self.c1}, {self.r2}, {self.c2})"

    def __lt__(self, other):
        if self.r1 == other.r1:
            return self.c1 < other.c1
        return self.r1 < other.r1


def subtract_rectangle(empty, stamp):   # 빈 영역에 스탬프를 찍었을때, 남은 빈 직사각 영역들을 반환
    ir1 = max(empty.r1, stamp.r1)
    ic1 = max(empty.c1, stamp.c1)
    ir2 = min(empty.r2, stamp.r2)
    ic2 = min(empty.c2, stamp.c2)

    # 겹치지 않음
    if ir1 > ir2 or ic1 > ic2:
        return [empty]

    result = []

    # 오른쪽 (c축 기준)
    if ic2 < empty.c2:
        result.append(Rectangle(empty.r1, ic2 + 1, empty.r2, empty.c2))

    # 왼쪽 (c축 기준)
    if ic1 > empty.c1:
        result.append(Rectangle(empty.r1, empty.c1, empty.r2, ic1 - 1))

    # 위쪽 (r축 기준)
    if ir1 > empty.r1:
        result.append(Rectangle(empty.r1, ic1, ir1 - 1, ic2))

    # 아래쪽 (r축 기준)
    if ir2 < empty.r2:
        result.append(Rectangle(ir2 + 1, ic1, empty.r2, ic2))

    return result

# 새롭게 추가된 클린업 함수
def merge_rectangles(rects):
    if not rects:
        return []

    merged = True
    # 더 이상 합쳐지는 조각이 없을 때까지 반복
    while merged:
        merged = False

        # 1. 가로 병합 (r축 기준 높이와 위치가 완벽히 같은 조각들을 딕셔너리로 묶기)
        row_groups = {}
        for r in rects:
            key = (r.r1, r.r2)
            if key not in row_groups:
                row_groups[key] = []
            row_groups[key].append(r)

        next_rects = []
        for key, group in row_groups.items():
            # 같은 그룹 내에서 왼쪽(c1)에서 오른쪽 순으로 정렬
            # group.sort(key=lambda x: x.c1)
            # lambda 대신 C 내장 모듈 사용 (가로 정렬)
            group.sort(key=operator.attrgetter('c1'))
            merged_group = [group[0]]

            for i in range(1, len(group)):
                prev = merged_group[-1]
                curr = group[i]
                # 직전 조각의 오른쪽 끝과 현재 조각의 왼쪽 끝이 정확히 맞닿아 있다면
                if prev.c2 + 1 == curr.c1:
                    # 하나로 합친 새로운 직사각형으로 덮어씌움
                    merged_group[-1] = Rectangle(prev.r1, prev.c1, prev.r2, curr.c2)
                    merged = True
                else:
                    merged_group.append(curr)
            next_rects.extend(merged_group)

        rects = next_rects

        # 2. 세로 병합 (c축 기준 너비와 위치가 완벽히 같은 조각들을 딕셔너리로 묶기)
        col_groups = {}
        for r in rects:
            key = (r.c1, r.c2)
            if key not in col_groups:
                col_groups[key] = []
            col_groups[key].append(r)

        next_rects = []
        for key, group in col_groups.items():
            # 같은 그룹 내에서 위(r1)에서 아래 순으로 정렬
            # group.sort(key=lambda x: x.r1)
            # lambda 대신 C 내장 모듈 사용 (세로 정렬)
            group.sort(key=operator.attrgetter('r1'))
            merged_group = [group[0]]

            for i in range(1, len(group)):
                prev = merged_group[-1]
                curr = group[i]
                # 직전 조각의 아래쪽 끝과 현재 조각의 위쪽 끝이 정확히 맞닿아 있다면
                if prev.r2 + 1 == curr.r1:
                    # 하나로 합친 새로운 직사각형으로 덮어씌움
                    merged_group[-1] = Rectangle(prev.r1, prev.c1, curr.r2, prev.c2)
                    merged = True
                else:
                    merged_group.append(curr)
            next_rects.extend(merged_group)

        rects = next_rects

    return rects


def solution(m, n, h, w, drops):
    # m이 행(r)의 개수, n이 열(c)의 개수
    empty = [Rectangle(0, 0, m - h, n - w)]   # 빈영역 - 선인장 시작점이 들어갈 수 있는 위치 기준

    for r, c in drops:
        next_empty = []
        # r, c에 비가 내렸다면, 선인장 좌상단 좌표(r, c)의 범위는
        # r축(세로)으로는 h만큼, c축(가로)으로는 w만큼의 영향을 받음
        stamp = Rectangle(r - h + 1, c - w + 1, r, c)

        for area in empty:
            next_empty.extend(subtract_rectangle(area, stamp))

        # 만약 이때 모든 영역이 젖었다면, 기존 젖은 영역 중에서 가장 상단 - 좌측을 찾음
        if not next_empty:
            empty.sort()
            return empty[0].r1, empty[0].c1

        # 클린업
        next_empty = merge_rectangles(next_empty)

        empty = next_empty

    # 젖지 않은 영역 중에서 가장 상단 - 좌측
    empty.sort()
    return empty[0].r1, empty[0].c1