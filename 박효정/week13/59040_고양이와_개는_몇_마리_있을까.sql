# 문제: 고양이와 개는 몇 마리 있을까
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59040

SELECT
    ANIMAL_TYPE,
    COUNT(*) AS count
FROM
    ANIMAL_INS
WHERE
    ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY
    ANIMAL_TYPE
ORDER BY
    CASE WHEN ANIMAL_TYPE = 'Cat' THEN 0 ELSE 1 END;
    # Cat일때는 0, Dog일때는 1이 되어서 오른차순으로 정렬하면 0부터 정렬(Cat)됨 