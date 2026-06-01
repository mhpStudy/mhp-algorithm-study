/**
* 문제: 시저 암호
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12926
* [성능 요약] 메모리: 60.9 MB 시간: 1.11 ms 
*/
public class Solution {

	public String solution(String s, int n) {
		StringBuilder sb = new StringBuilder();

		for (char c : s.toCharArray()) {
			if (Character.isUpperCase(c)) {
				sb.append((char) ((c - 'A' + n) % 26 + 'A'));
			} else if (Character.isLowerCase(c)) {
				sb.append((char) ((c - 'a' + n) % 26 + 'a'));
			} else {
				sb.append(" ");
			}
		}

		return sb.toString();
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("a B z", 4));
	}
}

