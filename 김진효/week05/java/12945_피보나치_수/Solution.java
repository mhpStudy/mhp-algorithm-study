/**
* 문제: 피보나치 수
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12945
* [성능 요약] 메모리: 663 MB 시간: 199.90 ms 
*/

import java.math.BigInteger;

public class Solution {

	public int solution(int n) {
		BigInteger[] f = new BigInteger[n + 1];

		f[0] = new BigInteger("0");
		f[1] = new BigInteger("1");

		for (int i = 2; i < n + 1; i++) {
			f[i] = f[i - 2].add(f[i-1]);
		}

		return f[n].remainder(new BigInteger("1234567")).intValue();
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(6));
	}
}
