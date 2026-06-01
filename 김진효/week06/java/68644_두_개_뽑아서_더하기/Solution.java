/**
* 문제: 두 개 뽑아서 더하기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/68644
* [성능 요약] 메모리: 61.9 MB 시간: 4.05 ms 
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

	public int[] solution(int[] numbers) {
		List<Integer> answer = new ArrayList<Integer>();

		int l = numbers.length;

		for (int i = 0; i < l; i++) {
			for (int j = i + 1; j < l; j++) {
				int sum = numbers[i] + numbers[j];
				if (!answer.contains(sum)) {
					answer.add(sum);
				}
			}

		}

		answer.sort(null);
		
		return answer.stream().mapToInt(i -> i).toArray();
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(Arrays.toString(s.solution(new int[] { 2, 1, 3, 4, 1 })));
	}
}