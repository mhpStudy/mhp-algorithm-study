/**
* 문제: 최솟값 만들기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12941
* [성능 요약] 메모리: 56.3 MB 시간: 2.68 ms 
*/

import java.util.ArrayList;

public class Solution {

	public int solution(int[] A, int[] B) {
		int answer = 0;
		ArrayList<Integer> a = new ArrayList<Integer>();
		for (Integer num : A) {
			a.add(num);
		}

		ArrayList<Integer> b = new ArrayList<Integer>();
		for (Integer num : B) {
			b.add(num);
		}

		a.sort(null);
		b.sort((i, j) -> j - i);

		for (int i = 0; i < A.length; i++) {
			answer += a.get(i) * b.get(i);
		}

		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(new int[] { 1, 4, 2 }, new int[] { 5, 4, 4 }));
	}
}
