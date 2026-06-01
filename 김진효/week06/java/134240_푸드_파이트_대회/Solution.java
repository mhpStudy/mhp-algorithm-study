/**
* 문제: 푸드 파이트 대회
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/134240
* [성능 요약] 메모리: 60 MB 시간: 0.79 ms 
*/

public class Solution {

	public String solution(int[] food) {
		StringBuilder answer = new StringBuilder();
		for (int i = 1; i < food.length; i++) {
			for (int j = 0; j < (int) food[i] / 2; j++) {
				answer.append(i);
			}
		}

		answer.append('0');

		for (int i = answer.length() - 2; i > -1; i--) {
			answer.append(answer.charAt(i));
		}

        // 위 answer을 sb로 두고
		// String answer = sb + "0";
		// answer += sb.reverse();


		return answer.toString();
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(new int[] { 1, 3, 4, 6 }));
	}
}