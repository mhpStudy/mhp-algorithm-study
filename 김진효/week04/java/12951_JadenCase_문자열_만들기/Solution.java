/**
* 문제: JadenCase 문자열 만들기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12951
* [성능 요약] 메모리: 60.1 MB 시간: 0.17 ms 
*/

public class Solution {

	public String solution(String s) {
		StringBuilder sb = new StringBuilder();
		
		s = s.toLowerCase();
		char[] charArr = s.toCharArray();
		
		sb.append(String.valueOf(charArr[0]).toUpperCase());
		
		for (int i = 1; i < charArr.length; i++) {
			if(charArr[i-1]==' ' && charArr[i] != ' ') {
				sb.append(String.valueOf(charArr[i]).toUpperCase());
			}else {
				sb.append(charArr[i]);
			}
		}
	
		return sb.toString();
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("  3people   unFollowed   me  "));
	}
}
