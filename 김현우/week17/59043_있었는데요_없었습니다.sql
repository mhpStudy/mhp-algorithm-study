-- 문제: 있었는데요 없었습니다
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/59043

-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS O
    ON A.ANIMAL_ID = O.ANIMAL_ID
WHERE A.DATETIME > O.DATETIME
ORDER BY A.DATETIME