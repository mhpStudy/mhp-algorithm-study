-- 문제: 경기도에 위치한 식품창고 목록 출력하기
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/131114

-- 통용
SELECT warehouse_id, warehouse_name, address, COALESCE(freezer_yn,'N') as "FREEZER_YN" 
FROM food_warehouse 
WHERE address LIKE '%경기%' 
ORDER BY warehouse_id;

-- oracle
SELECT warehouse_id, warehouse_name, address, NVL(freezer_yn,'N') as "FREEZER_YN" 
FROM food_warehouse 
WHERE address LIKE '%경기%' 
ORDER BY warehouse_id;

-- mysql
SELECT warehouse_id, warehouse_name, address, IFNULL(freezer_yn,'N') as "FREEZER_YN" 
FROM food_warehouse 
WHERE address LIKE '%경기%' 
ORDER BY warehouse_id;