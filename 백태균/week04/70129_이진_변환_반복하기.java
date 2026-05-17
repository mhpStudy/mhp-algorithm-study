class Solution {
    public int[] solution(String s) {
        int[] answer = {};

        // Integer.toBinaryString: 10진수에서 2진수로 변환
        // Integer.parseInt("1010", 2): 2진수에서 원하는 10진수로 변환

        int cntRound = 0;  // 이진 변환의 횟수 저장하는 변수
        int cntZero = 0;  // 변환 과정에서 제거된 모든 0의 개수 저장하는 변수

        while (s.length() != 1) {  // 길이가 한 자릿수일 때까지 순회하면서
            StringBuilder sb = new StringBuilder();

            for (int i=0; i<s.length(); i++) {  // 현재 s의 길이 만큼 순회하면서
                if (s.charAt(i) != '0') {  // 1이면
                    sb.append(s.charAt(i));  // sb에 추가
                } else {  // 0이면
                    cntZero++;  // 제거된 0의 개수 증가
                }
            }

            // 현재 문장의 길이의 2진수를 구해야하니깐
            int len = sb.length();  // 길이 구한 다음에
            s = Integer.toBinaryString(len);  // 10진수에서 2진수로 변환
            cntRound++;  // 이진 변환의 횟수 증가
        }

        return new int[]{cntRound, cntZero};
    }
}