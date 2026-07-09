# 문제: 가격이 제일 비싼 식품의 정보 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/131115

SELECT datetime FROM animal_ins ORDER BY datetime FETCH FIRST ROW 1 ONLY

SELECT datetime as "시간"
FROM animal_ins
WHERE
    datetime = (
        SELECT MIN(datetime)
        FROM animal_ins
    )