# 문제: 카테고리 별 도서 판매량 집계하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/144855

SELECT b.category as "CATEGORY", SUM(s.sales) as "TOTAL_SALES"
FROM book b
    JOIN book_sales s ON b.book_id = s.book_id
WHERE
    TO_CHAR (s.sales_date, 'YYYY-MM') = '2022-01'
GROUP BY
    b.category
ORDER BY b.category;