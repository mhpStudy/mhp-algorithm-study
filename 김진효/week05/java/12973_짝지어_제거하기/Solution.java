/**
* 문제: 짝지어 제거하기
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12973
* [성능 요약] 메모리: 67.7 MB 시간: 33.84 ms 
*/
import java.util.Stack;

public class Solution {

	public int solution(String s) {
		Stack<Character> stack = new Stack<Character>();

		stack.add('0');

		for (char c : s.toCharArray()) {
			if (stack.peek() != c) {
				stack.add(c);
			} else {
				stack.pop();
			}
		}

		return stack.peek() == '0' ? 1 : 0;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("cdcd"));
	}
}
