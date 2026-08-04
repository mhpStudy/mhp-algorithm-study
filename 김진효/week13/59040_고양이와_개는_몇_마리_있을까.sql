# 문제: 고양이와 개는 몇 마리 있을까
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59040

SELECT animal_type, COUNT(*) as count
FROM animal_ins
GROUP BY
    animal_type
order by animal_type;


-- 더 엄격하게
SELECT animal_type, COUNT(*) as count
FROM animal_ins
WHERE
    LOWER(animal_type) IN ('cat', 'dog')
GROUP BY
    animal_type
order by animal_type;