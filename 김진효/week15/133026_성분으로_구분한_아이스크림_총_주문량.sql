# 문제: 성분으로 구분한 아이스크림 총 주문량
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/133026

SELECT i.ingredient_type as "INGREDIENT_TYPE", SUM(f.total_order) as "TOTAL_ORDER"
FROM first_half f
    JOIN icecream_info i ON f.flavor = i.flavor
GROUP BY
    i.ingredient_type
ORDER BY 2; 