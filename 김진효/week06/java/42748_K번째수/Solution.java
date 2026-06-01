/**
* 문제: K번째수
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/42748
* [성능 요약] 메모리: 62.3 MB 시간: 0.03 ms 
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

	public int[] solution(int[] array, int[][] commands) {
		int[] answer = new int[commands.length];

		for (int i = 0; i < commands.length; i++) {
			List<Integer> list = new ArrayList<Integer>();
			for (int j = commands[i][0] - 1; j < commands[i][1]; j++) {
				list.add(array[j]);
			}
			list.sort(null);
			answer[i] = list.get(commands[i][2] - 1);
		}
		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(Arrays.toString(
				s.solution(new int[] { 1, 5, 2, 6, 3, 7, 4 }, new int[][] { { 2, 5, 3 }, { 4, 4, 1 }, { 1, 7, 3 } })));
	}
}
