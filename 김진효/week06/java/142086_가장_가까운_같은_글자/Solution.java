/**
* 문제: 가장 가까운 같은 글자
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/142086
* [성능 요약] 메모리: 65.2 MB 시간: 1.89 ms 
*/
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {

	public int[] solution(String s) {
		int[] answer = new int[s.length()];

		// 알파벳을 담은 hashmap 생성
		Map<Character, Integer> m = new HashMap<Character, Integer>();
		for (int i = 'a'; i < 'z' + 1; i++) {
			m.put((char) i, -1);
		}

		int idx = 0;
		for (char c : s.toCharArray()) {
			int pre = m.get(c);
			if (pre == -1) {
				answer[idx] = -1;
			} else {
				answer[idx] = idx - pre;
			}
			m.put(c, idx);
			idx++;
		}

		return answer;
	}

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(Arrays.toString(s.solution("banana")));
	}
}