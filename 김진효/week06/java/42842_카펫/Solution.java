/**
* 문제: 카펫
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/42842
* [성능 요약] 메모리: 62.6 MB 시간: 0.04 ms 
*/
import java.util.Arrays;

public class Solution {

	public int[] solution(int brown, int yellow) {
		for (int i = 1; i < (int) Math.sqrt(yellow) + 1; i++) {
			if (yellow % i == 0) {
				int w = yellow / i + 2;
				int h = i + 2;

				if (2 * w + 2 * h - 4 == brown) {
					return new int[] { w, h };
				}
			}
		}
		return new int[] {};
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(Arrays.toString(s.solution(24, 24)));
	}
}
