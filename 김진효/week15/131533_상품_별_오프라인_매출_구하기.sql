# 문제: 상품 별 오프라인 매출 구하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131533

SELECT p.product_code as "PRODUCT_CODE", SUM(o.sales_amount * price) as "SALES"
FROM product p
    JOIN offline_sale o ON p.product_id = o.product_id
GROUP BY
    p.product_code
ORDER BY 2 desc, 1 asc;