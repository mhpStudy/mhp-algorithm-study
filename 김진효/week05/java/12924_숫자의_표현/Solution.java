/**
* 문제: 숫자의 표현
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12924
* [성능 요약] 메모리: 56.3 MB 시간: 0.31 ms 
*/

public class Solution {

	public int solution(int n) {
		int start = 1;
		int end = 1;
		int cnt = 1;
		int sum = 1;

		while (end != n) {
			if (sum == n) {
				cnt++;
				end++;
				sum += end;
			} else if (sum > n) {
				sum -= start;
				start++;
			} else if (sum < n) {
				end++;
				sum += end;
			}
		}

		return cnt;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(15));
	}
}
