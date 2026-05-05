
/**
* 문제: 행렬의 덧셈
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12950
* [성능 요약] 메모리: 143 MB 시간: 4.12 ms 
*/
import java.util.Arrays;

public class Solution {

	public int[][] solution(int[][] arr1, int[][] arr2) {
		int[][] answer = new int[arr1.length][arr1[0].length];
		for (int i = 0; i < arr1.length; i++) {
			for (int j = 0; j < arr1[0].length; j++) {
				answer[i][j] = arr1[i][j] + arr2[i][j];
			}
		}

		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		int[][] arr1 = new int[2][2];
		arr1[0] = new int[] { 1, 2 };
		arr1[1] = new int[] { 2, 3 };

		int[][] arr2 = new int[2][2];
		arr2[0] = new int[] { 3, 4 };
		arr2[1] = new int[] { 5, 6 };

		System.out.println(Arrays.deepToString(s.solution(arr1, arr2)));
	}
}
