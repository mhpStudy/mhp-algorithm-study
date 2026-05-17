/**
* 문제: 크기가 작은 부분 문자열
* URL: https://school.programmers.co.kr/learn/courses/30/lessons/147355
* [성능 요약] 메모리: 66 MB 시간: 4.31 ms 
*/
public class Solution {

    public int solution(String t, String p) {
        int answer = 0;
        int l = p.length();
        Long num = Long.parseLong(p);
        
        for (int i = 0; i < t.length()-l+1; i++) {
        	Long target = Long.parseLong(t.substring(i, i+l));
        	if(target <= num) {
        		answer += 1;
        	}
			
		}
        return answer;
    }

	public static void main(String[] args) {
		Solution s = new Solution();
		// 테스트 케이스를 입력하세요
		System.out.println(s.solution("3141592","271"));
	}
}
