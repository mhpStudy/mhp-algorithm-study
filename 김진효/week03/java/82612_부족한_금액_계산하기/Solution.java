
/**
* 문제: 부족한 금액 계산하기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/82612
* [성능 요약] 메모리: 90.5 MB 시간: 13.02 ms 
*/
public class Solution {
    
	public long solution(int price, int money, int count) {
		long answer = 0;
		long s = 0;
		for (long p = price; p < price * count + 1; p += price) {
			System.out.println(p);
			s += p;
		}

		return (s <= money) ? answer : s - money;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(3, 20, 4));
	}
}
