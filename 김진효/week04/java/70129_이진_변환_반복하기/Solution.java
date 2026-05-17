/**
* 문제: 이진 변환 반복하기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/70129
* [성능 요약] 메모리: 61.9 MB 시간: 5.00 ms
*/

import java.util.Arrays;

public class Solution {

	public int[] solution(String s) {
		int[] answer = new int[2];

		int binCnt = 0;
		int zeroCnt = 0;

		while (!s.equals("1")) {

			// 0 제거
			StringBuilder sb = new StringBuilder();
			for (char c : s.toCharArray()) {
				if (c == '0') {
					zeroCnt += 1;
				} else {
					sb.append(c);
				}
			}

			// 이진수로 변환
			int c = sb.length();

			StringBuilder binStr = new StringBuilder();
			while (c > 0) {
				binStr.append(c % 2);
				c /= 2;
			}

			s = binStr.reverse().toString();

			binCnt += 1;

		}

		//System.out.println(binCnt+" "+zeroCnt);

		answer[0] = binCnt;
		answer[1] = zeroCnt;

		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(Arrays.toString(s.solution("0111010")));
		System.out.println(Arrays.toString(s.solution("110010101001")));
		System.out.println(Arrays.toString(s.solution("01110")));
		System.out.println(Arrays.toString(s.solution("1111111")));

	}
}
