class Solution {
    public int solution(String t, String p) {

        StringBuilder sb = new StringBuilder(t);  // 문자열 문법을 사용하기 위해 StringBuilder로 변환
        int until = t.length() - p.length();  // 부분 문자열 탐색의 마지막 인덱스
        int cnt = 0;  // 작거나 같은 것이 나오는 횟수 카운트

        for (int i=0; i<=until; i++) {  // until까지 순회하면서
            long test = Long.parseLong(sb.substring(i, i+p.length()));  // 현재 위치에서 p의 길이만큼 자르고 long 타입으로 변환

            if (test <= Long.parseLong(p)) {  // p보다 작거나 같은 수면
                cnt++;  // 카운트 수 증가
            }
        }

        return cnt;
    }
}