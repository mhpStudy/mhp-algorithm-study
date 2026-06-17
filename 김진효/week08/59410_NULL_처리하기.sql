# 문제: NULL 처리하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59410

-- Oracle: NVL
SELECT
    animal_type,
    NVL (name, 'No name') as "NAME",
    sex_upon_intake
FROM ANIMAL_INS
ORDER BY animal_id

-- MySQL: IFNULL
SELECT
    animal_type,
    IFNULL(name, 'No name') as "NAME",
    sex_upon_intake
FROM ANIMAL_INS
ORDER BY animal_id

--COLLAPSE
SELECT
    animal_type,
    COALESCE(name, 'No name') as "NAME",
    sex_upon_intake
FROM ANIMAL_INS
ORDER BY animal_id