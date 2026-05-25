/**
* 문제: 삼총사
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/131705
* [성능 요약] 메모리: 63.8 MB 시간: 0.47 ms 
*/
public class Solution {

	private int cnt;
	private boolean[] used;
	private int[] number;

	public int solution(int[] number) {
		int l = number.length;

		this.cnt = 0;
		this.used = new boolean[l];
		this.number = number;

		recur(0, 0, 0, l);

		return cnt;
	}

	// 재귀
	public void recur(int n, int s, int start, int l) {
		if (n == 3) {
			if (s == 0) {
				cnt += 1;
				return;
			}
		}

		for (int i = start; i < l; i++) {
			if (!used[i]) {
				used[i] = true;
				recur(n + 1, s + number[i], i + 1, l);
				used[i] = false;
			}

		}

	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(new int[] { -2, 3, 0, 2, -5 }));
	}
}
