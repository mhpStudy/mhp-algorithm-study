/**
* 문제: 콜라 문제
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/132267
* [성능 요약] 메모리: 63.4 MB 시간: 0.07 ms 
*/

public class Solution {

	public int solution(int a, int b, int n) {
		int answer = 0;
		int plus = 0;
		while (n >= a) {
			plus = n / a;
			n = plus * b + n % a;
			answer += plus * b;
		}
		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(2, 1, 20));
	}
}
