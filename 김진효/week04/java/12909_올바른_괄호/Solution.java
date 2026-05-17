/**
* 문제: 올바른 괄호
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12909
# [성능 요약] 메모리: 56.9 MB 시간: 8.48 ms
*/

import java.util.Stack;

public class Solution {

	boolean solution(String s) {
		boolean answer = true;

		if (s.charAt(0) == ')') {
			return false;
		}

		Stack<String> stack = new Stack<String>();

		for (char c : s.toCharArray()) {
			if (c == '(') {
				stack.add(s);
			} else {
				if (stack.empty()) {
					return false;
				} else {
					stack.pop();
				}
			}
		}

		if (!stack.empty()) {
			return false;
		}

		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("()()"));
		System.out.println(s.solution("(())()"));
		System.out.println(s.solution(")()("));
		System.out.println(s.solution("(()("));
	}
}