
/**
* 문제: 문자열 다루기 기본
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12918
* [성능 요약] 메모리: 80.1 MB 시간: 0.14 ms 
*/
public class Solution {

	public boolean solution(String s) {
        return s.matches("[0-9]{4}|[0-9]{6}");
    }

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("231a"));
	}
}
