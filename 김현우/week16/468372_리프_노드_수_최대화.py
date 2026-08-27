# 문제: 리프 노드 수 최대화
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/468372

def solution(dist_limit, split_limit):
    # 가능한 2의 거듭제곱
    pow2 = [1]
    while pow2[-1] * 2 <= split_limit:
        pow2.append(pow2[-1] * 2)

    # 가능한 3의 거듭제곱
    pow3 = [1]
    while pow3[-1] * 3 <= split_limit:
        pow3.append(pow3[-1] * 3)

    answer = 1

    # i = 2분배 층 수
    # j = 3분배 층 수
    for i, p2 in enumerate(pow2):
        for j, p3 in enumerate(pow3):

            # 가장 깊은 리프의 분배도
            if p2 * p3 > split_limit:
                break

            # -----------------------------------
            # 경우 1
            #
            # 2 → 2 → ... → [2 부분분배] → 3 → 3 → ...
            #
            # 부분 분배가 2 블록의 마지막에서 발생
            # 이후 3 블록은 완전 분배
            # -----------------------------------
            if i > 0:
                # 마지막 2분배 직전 frontier
                #
                # i=3이면:
                # 1 → 2 → 4
                #          ↑ 여기
                w = pow2[i - 1]

                # 여기까지 오는 데 사용한 분배 노드
                #
                # 1 + 2 + 4 + ... + 2^(i-2)
                # = 2^(i-1) - 1
                used = w - 1

                if used <= dist_limit:
                    # w개 중 a개만 2분배한다고 하자.
                    #
                    # 한 노드를 2분배한 뒤
                    # j개의 3분배 층을 전부 통과시키는 데 필요한 비용:
                    #
                    # 1 + 2 + 2*3 + ... + 2*3^(j-1)
                    # = 3^j
                    #
                    # 따라서 a <= (남은 예산) // 3^j
                    a = min(
                        w,
                        (dist_limit - used) // p3
                    )

                    # 분배하지 않은 노드:
                    # w - a
                    #
                    # 분배한 노드:
                    # a → 2a → 2a*3^j
                    #
                    # 총 리프
                    # = (w-a) + 2a*3^j
                    # = w + a(2*3^j - 1)
                    leaves = w + a * (2 * p3 - 1)

                    answer = max(answer, leaves)

            # -----------------------------------
            # 경우 2
            #
            # 2 → ... → 2 → 3 → ... → [3 부분분배]
            #
            # 2 블록은 전부 완전 분배
            # 마지막 3 층에서 부분 분배
            # -----------------------------------
            if j > 0:
                # 마지막 3분배 직전 frontier
                prev_p3 = pow3[j - 1]

                w = p2 * prev_p3

                # 2 블록을 완전히 만드는 비용
                #
                # 1 + 2 + ... + 2^(i-1)
                # = 2^i - 1
                used_2 = p2 - 1

                # 그 뒤 j-1개의 3 층을 완전히 만드는 비용
                #
                # 2^i * (1 + 3 + ... + 3^(j-2))
                used_3 = p2 * (prev_p3 - 1) // 2

                used = used_2 + used_3

                if used <= dist_limit:
                    # 남은 예산만큼 마지막 3분배 수행
                    a = min(
                        w,
                        dist_limit - used
                    )

                    # 3분배 하나당
                    # 리프 1개 → 3개
                    # 즉 +2
                    leaves = w + 2 * a

                    answer = max(answer, leaves)

    return answer