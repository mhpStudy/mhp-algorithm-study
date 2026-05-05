
/**
* 문제: 같은 숫자는 싫어
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12906
* [성능 요약] 메모리: 115 MB 시간: 20.40 ms 
* 정확성: 71.9
* 효율성: 28.1
*/

import java.util.ArrayList;

public class Solution {

    public ArrayList<Integer> solution(int []arr) {
        ArrayList<Integer> li = new ArrayList<Integer>();
        
        li.add(arr[0]);
        
        for (int i = 1; i < arr.length; i++) {
			if(arr[i] != arr[i-1]) {
				li.add(arr[i]);
			}
		}

		return li;
    }

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution(new int[] {1,1,3,3,0,1,1}));
	}
}