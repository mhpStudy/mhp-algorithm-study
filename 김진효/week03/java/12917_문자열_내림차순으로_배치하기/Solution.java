
/**
* 문제: 문자열 내림차순으로 배치하기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12917
* [성능 요약] 메모리: 70 MB 시간: 1.43 ms 
*/

import java.util.ArrayList;

public class Solution {

	public String solution(String s) {
		StringBuilder sb = new StringBuilder();
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			arr.add((int) c);
		}
		arr.sort((a, b) -> b - a);

		for (int n : arr) {
			sb.append((char) n);
		}

		return sb.toString();
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("Zbcdefg"));
	}
}
