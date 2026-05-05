
/**
* 문제: 내적
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/70128
* [성능 요약] 메모리: 84.2 MB 시간: 0.04 ms 
*/

public class Solution {

	public int solution(int[] a, int[] b) {
		int answer = 0;

		for (int i = 0; i < b.length; i++) {
			answer += a[i] * b[i];

		}
		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(new int[] { 1, 2, 3, 4 }, new int[] { -3, -1, 0, 2 }));
	}
}
