# 문제: 최솟값 구하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59038

SELECT * FROM food_product 
ORDER BY price DESC 
FETCH FIRST 1 ROW ONLY

SELECT *
FROM food_product
WHERE
    price = (
        SELECT MAX(price)
        FROM food_product
    )