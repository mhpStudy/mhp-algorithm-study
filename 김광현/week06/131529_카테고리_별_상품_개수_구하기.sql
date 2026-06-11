-- 문제: 카테고리 별 상품 개수 구하기
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/131529

-- substring이 뭔지 알기

-- 코드를 입력하세요
SELECT SUBSTRING(PRODUCT_CODE, 1, 2) AS CATEGORY,
       COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY SUBSTRING(PRODUCT_CODE, 1, 2)
ORDER BY CATEGORY;