# 문제: 중복 제거하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/59408

-- 코드를 입력하세요
SELECT count(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL