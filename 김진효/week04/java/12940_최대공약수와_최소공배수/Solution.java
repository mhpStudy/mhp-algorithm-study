/**
* 문제: 최대공약수와 최소공배수
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12940
* [성능 요약] 메모리: 63.3 MB 시간: 0.03 ms 
*/

import java.util.Arrays;

public class Solution {

	public int[] solution(int n, int m) {
		int[] answer = new int[2];

		// 최대 공약수
		int a = n;
		int b = m;

		int temp = b;
		while (b > 0) {
			b = a % b;
			a = temp;
			temp = b;
		}

		answer[0] = a;

		// 최소 공배수
		answer[1] = n * m / answer[0];

		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(Arrays.toString(s.solution(3, 12)));
	}
}
