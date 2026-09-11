-- 문제: 3월에 태어난 여성 회원 목록 출력하기
-- URL: https://school.programmers.co.kr/learn/courses/30/lessons/131120

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3
  AND GENDER = 'W'
  AND TLNO IS NOT NULL
ORDER BY MEMBER_ID

