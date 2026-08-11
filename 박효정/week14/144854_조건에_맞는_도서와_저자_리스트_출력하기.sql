# 문제: 조건에 맞는 도서와 저자 리스트 출력하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT
    BOOK.BOOK_ID,
    AUTHOR.AUTHOR_NAME,
    TO_CHAR(BOOK.PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM 
    BOOK
JOIN 
    AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE
    BOOK.CATEGORY = '경제'
ORDER BY
    PUBLISHED_DATE;
    