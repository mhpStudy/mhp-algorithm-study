/**
* 문제: 다음 큰 숫자
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12911
* [성능 요약] 메모리: 63.5 MB 시간: 0.05 ms 
*/
public class Solution {

	public int solution(int n) {
		int answer = 0;
		String b = Integer.toBinaryString(n);
		int oneCnt = countOne(b);
		while (true) {
			n++;
			if (countOne(Integer.toBinaryString(n)) == oneCnt) {
				answer = n;
				break;
			}
		}
		return answer;
	}

	public int countOne(String s) {
		int cnt = 0;
		for (char c : s.toCharArray()) {
			if (c == '1')
				cnt++;
		}
		return cnt;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(78));
	}
}
