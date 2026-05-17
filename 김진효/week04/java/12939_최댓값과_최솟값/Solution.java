/**
* 문제: 최댓값과 최솟값
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12939
* [성능 요약] 메모리: 60.1 MB 시간: 9.93 ms 
*/

public class Solution {

	public String solution(String s) {
		String[] sl =  s.split(" ");
		
		// 배열의 첫 번째 값으로 초기화
		int maxValue = Integer.parseInt(sl[0]);
		int minValue = Integer.parseInt(sl[0]);
		
		for (int i = 1; i < sl.length; i++) {
			int value = Integer.parseInt(sl[i]);
			// 최대값 찾기
			if(maxValue < value ) {
				maxValue = value;
			}
			
			// 최소값 찾기
			if(minValue > value) {
				minValue = value;
			}
		}
		
		return minValue+" "+maxValue;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("1 2 3 4"));
	}
}
