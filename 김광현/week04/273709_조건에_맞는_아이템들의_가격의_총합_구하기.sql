-- 문제: 조건에 맞는 아이템들의 가격의 총합 구하기
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/273709

SELECT SUM(PRICE)
FROM ITEM_INFO
WHERE RARITY = "LEGEND"