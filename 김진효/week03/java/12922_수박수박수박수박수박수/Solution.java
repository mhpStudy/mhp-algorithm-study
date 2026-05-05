
/**
* 문제: 수박수박수박수박수박수?
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/12922
* 1: [성능 요약] 메모리: 135 MB 시간: 47.00 ms 
* 2: [성능 요약] 메모리: 87.7 MB 시간: 0.88 ms 
*/

public class Solution {
    
    /* 1. 바로 붙이기 */
    // public String solution(int n) {
    //     String answer = "";
    //     for (int i = 0; i < n; i++) {
	// 		if(i % 2==0) {
	// 			answer += '수';
	// 		}else {
	// 			answer += '박';
	// 		}
	// 	}

    //     return answer;
    // }

    /* 2. StringBuilder 사용 */
    public String solution(int n) {
        StringBuilder sb = new StringBuilder();
    	for (int i = 0; i < n; i++) {
			if(i % 2==0) {
				sb.append('수');
			}else {
				sb.append('박');
			}
		}
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        // 테스트 케이스를 입력하세요
        System.out.println(s.solution(0));
    }
}

