# 문제: 진료과별 총 예약 횟수 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/132202

SELECT mcdp_cd "진료과코드", COUNT(*) as "5월예약건수"
FROM appointment
WHERE
    apnt_ymd >= TO_DATE ('2022-05-01', 'YYYY-MM-DD')
    AND apnt_ymd < TO_DATE ('2022-06-01', 'YYYY-MM-DD')
GROUP BY
    mcdp_cd
ORDER BY "5월예약건수", mcdp_cd;

-- 날짜 형식 -> TO_CHAR 이용
SELECT mcdp_cd "진료과코드", COUNT(*) as "5월예약건수"
FROM appointment
WHERE
    TO_CHAR (apnt_ymd, 'YYYY-MM') = '2022-05'
GROUP BY
    mcdp_cd
ORDER BY "5월예약건수", mcdp_cd;