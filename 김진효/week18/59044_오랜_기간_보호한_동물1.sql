# 문제: 오랜 기간 보호한 동물(1)
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59044

-- left outer join
SELECT *
FROM (
        SELECT i.name as "NAME", i.datetime as "DATETIME"
        FROM animal_ins i, animal_outs o
        WHERE
            i.animal_id = o.animal_id (+)
            AND o.animal_id IS NULL
        ORDER BY i.datetime FETCH FIRST 3 ROWS ONLY
    )
ORDER BY datetime;