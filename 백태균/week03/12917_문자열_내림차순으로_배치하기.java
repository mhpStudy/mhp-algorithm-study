import java.util.*;

class Solution {
    public String solution(String s) {

        char[] c = s.toCharArray();  // char 배열로 생성
        Arrays.sort(c);  // 오름차순으로 정렬

        char[] answer = new char[c.length];  // 내림차순으로 만들 char 배열 생성
        int idx = 0;  // 처음부터 넣어야 하니깐 새로운 인덱스 변수 생성

        for (int i=c.length-1; i>=0; i--) {  // c 배열의 뒤에서부터 시작
            answer[idx] = c[i];  // answer의 배열에 처음부터 차례대로 넣기
            idx++;
        }

        return String.valueOf(answer);  // String 타입으로 변환 후 반환
    }
}