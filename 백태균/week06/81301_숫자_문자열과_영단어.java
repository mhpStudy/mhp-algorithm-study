import java.util.*;

class Solution {

    static Map<String, String> map = Map.of(
            "zero", "0",
            "one", "1",
            "two", "2",
            "three", "3",
            "four", "4",
            "five", "5",
            "six", "6",
            "seven", "7",
            "eight", "8",
            "nine", "9"
    );

    public int solution(String s) {

        StringBuilder sb = new StringBuilder();  // 단어 구별하기 위한 변수
        StringBuilder answer = new StringBuilder();  // 정답 변수

        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) - '0' <= 9) {  //char를 숫자로 변환해서 9 이하이면
                answer.append(s.charAt(i));  // 숫자는 그냥 넣으면 되니깐 추가
                continue;
            }

            sb.append(s.charAt(i));  // char를 sb에 추가

            if (map.containsKey(sb.toString())) {  // 추가 했을 때 단어가 map 키 값에 있다면
                answer.append(map.get(sb.toString()));  // value값을 정답 변수에 추가
                sb = new StringBuilder();  // sb를 초기화
            }
        }

        return Integer.parseInt(answer.toString());  // int로 변환
    }
}