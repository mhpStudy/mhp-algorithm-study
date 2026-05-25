/**
* 문제: 3진법 뒤집기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/68935
* [성능 요약] 메모리: 62.8 MB 시간: 0.10 ms 
*/
public class Solution {

	public int solution(int n) {

		// 3진법
		StringBuilder t = new StringBuilder();
		while (n > 0) {
			t.append(n % 3);
			n /= 3;
		}

		// 10진법
		String temp = t.toString();
		int d = 0;
		int idx = temp.length() - 1;
		for (char c : temp.toCharArray()) {
			d += Character.getNumericValue(c) * (Math.pow(3, idx));
			idx--;
		}

		return d;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(45));
	}
}