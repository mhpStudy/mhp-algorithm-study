/**
* 문제: 이상한 문자 만들기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12930
* [성능 요약] 메모리: 63.7 MB 시간: 5.27 ms 
*/

public class Solution {

	public String solution(String s) {
		StringBuilder sb = new StringBuilder();
		s = " " + s + " ";
		int flag = -1;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == ' ') {
				sb.append(' ');
				continue;
			}

			// 첫글자일 경우 flag 설정
			if (s.charAt(i - 1) == ' ') {
				flag = 0;
			}

			if (flag % 2 == 0) {
				sb.append(Character.toUpperCase(s.charAt(i)));
			} else {
				sb.append(Character.toLowerCase(s.charAt(i)));
			}

			flag++;

		}
		
		
		return sb.substring(1, sb.length()-1).toString();
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("  try   hello   world  "));
	}
}
