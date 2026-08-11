# 문제: 입양 시각 구하기(1)
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59412

SELECT TO_NUMBER (TO_CHAR (datetime, 'HH24')) as "HOUR", COUNT(*) as "COUNT"
FROM ANIMAL_OUTS
WHERE
    TO_CHAR (datetime, 'HH24') BETWEEN '09' AND '19'
GROUP BY
    TO_CHAR (datetime, 'HH24')
ORDER BY 1;