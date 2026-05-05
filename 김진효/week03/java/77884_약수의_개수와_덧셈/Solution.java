
/**
* 문제: 약수의 개수와 덧셈
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/77884
* [성능 요약] 메모리: 79.3 MB 시간: 0.09 ms 
*/
public class Solution {

	public int solution(int left, int right) {
		int answer = 0;
		for (int num = left; num < right + 1; num++) {

			double numSqrt = Math.sqrt(num);
			if (numSqrt - (int) numSqrt > 0) {
				answer += num;
			} else {
				answer -= num;
			}
		}
		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println("Hello World");
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(13, 17));
	}
}
