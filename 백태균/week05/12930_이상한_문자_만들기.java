class Solution {
    public String solution(String s) {
        // 내가 실수한 것
        // 하나 이상의 공백문자로 구분되어 있다는 것을 인지 못함

        StringBuilder sb = new StringBuilder();
        int idx = 0;  // 띄어쓰기 기준으로 시작하는 인덱스 값

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if (c == ' ') {  // 만약에 띄어쓰기라면
                sb.append(" ");  // 띄어쓰기를 StringBuilder에 추가하고
                idx = 0;  // idx값을 0으로. 왜냐하면 띄어쓰기 다음에는 짝수값으로 되니깐
            } else {  // 만약에 띄어쓰기가 아니라 문자라면
                if (idx % 2 == 0) {  // 인덱스 값이 짝수일 때
                    sb.append(Character.toUpperCase(c));  // 대문자로 변경
                } else {  // 인덱스 값이 홀수일 때
                    sb.append(Character.toLowerCase(c));  // 소문자로 변경
                }

                idx++;  // 인덱스 값 올리기
            }
        }

        return sb.toString();
    }
}