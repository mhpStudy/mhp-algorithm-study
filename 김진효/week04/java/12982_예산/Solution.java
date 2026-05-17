/**
* 문제: 예산
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12982
*/
import java.util.Arrays;

public class Solution {

    // [성능 요약] 메모리: 62.7 MB 시간: 0.39 ms
	public int solution(int[] d, int budget) {
		int answer = 0;

		Arrays.sort(d);


		for (int p : d) {
			budget -= p;
			if (budget < 0) {
				return answer;
			}

			answer += 1;
		}

		return answer;
	}

	// [성능 요약] 메모리: 62.8 MB 시간: 0.36 ms
	public int solution2(int[] d, int budget) {
		int answer = 0;

        Arrays.sort(d);

		while (answer < d.length && budget > 0) {
			budget -= d[answer];
			answer += 1;
		}

		return (budget >= 0) ? answer : answer - 1;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution2(new int[] { 1, 3, 2, 5, 4 }, 9));
		System.out.println(s.solution2(new int[] { 2, 2, 3, 3 }, 10));
		System.out.println(s.solution2(new int[] { 2, 2, 3, 3 }, 30));
	}
}