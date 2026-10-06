# 문제: 조건에 맞는 사용자와 총 거래금액 조회하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/164668

SELECT u.user_id as "USER_ID", u.nickname as "NICKNAME", SUM(b.price) "TOTAL_SALES"
FROM
    used_goods_board b
    JOIN used_goods_user u ON b.writer_id = u.user_id
WHERE
    b.status = "DONE"
GROUP BY
    u.user_id
HAVING
    SUM(b.price) >= 700000
ORDER BY 3;