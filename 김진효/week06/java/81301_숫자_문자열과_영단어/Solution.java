/**
* 문제: 숫자 문자열과 영단어
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/81301
* [성능 요약] 메모리: 64.6 MB 시간: 0.07 ms 
*/
import java.util.HashMap;
import java.util.Map;

public class Solution {

	public int solution(String s) {
		Map<String, String> map = new HashMap<String, String>();

		// 진짜 java는 put으로 다 넣어야하는거..?
		map.put("zero", "0");
		map.put("one", "1");
		map.put("two", "2");
		map.put("three", "3");
		map.put("four", "4");
		map.put("five", "5");
		map.put("six", "6");
		map.put("seven", "7");
		map.put("eight", "8");
		map.put("nine", "9");

		for (String k : map.keySet()) {
			s = s.replace(k, map.get(k));
		}

		return Integer.parseInt(s);
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("one4seveneight"));
	}
}
