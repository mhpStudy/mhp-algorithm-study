
/**
* 문제: 제일 작은 수 제거하기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12935
* [성능 요약] 메모리: 103 MB 시간: 1.47 ms 
*/
import java.util.Arrays;

public class Solution {

	public int[] solution(int[] arr) {
		int[] answer = new int[arr.length - 1];

		if (arr.length == 1) {
			return new int[] { -1 };
		}

		// 최소값 먼저 찾기
		int minValue = arr[0];
		int minIdx = 0;
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] < minValue) {
				minValue = arr[i];
				minIdx = i;
			}

		}

		int idx = 0;
		for (int i = 0; i < arr.length; i++) {
			if (i == minIdx) {
				continue;
			}
			answer[idx] = arr[i];
			idx += 1;
		}

		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(Arrays.toString(s.solution(new int[] { 4, 3, 2, 1, 1})));
	}
}
