/**
* 문제: 최소직사각형
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/86491
* [성능 요약] 메모리: 67.5 MB 시간: 0.95 ms 
*/

public class Solution {

	public int solution(int[][] sizes) {
		//긴 변 끼리 배열 만들고 짧은 변 끼리 배열 만들기
		int[] arr1 = new int[sizes.length + 1];
		int[] arr2 = new int[sizes.length + 1];

		for (int i = 0; i < sizes.length; i++) {
			if (sizes[i][0] > sizes[i][1]) {
				arr1[i] = sizes[i][0];
				arr2[i] = sizes[i][1];
			} else {
				arr2[i] = sizes[i][0];
				arr1[i] = sizes[i][1];
			}
		}

		int maxW = 0;
		int maxH = 0;

		for (int n : arr1) {
			if (n > maxW) {
				maxW = n;
			}
		}

		for (int n : arr2) {
			if (n > maxH) {
				maxH = n;
			}
		}

		return maxW * maxH;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(new int[][] { { 60, 50 }, { 30, 70 }, { 60, 30 }, { 80, 40 } }));
	}
}
