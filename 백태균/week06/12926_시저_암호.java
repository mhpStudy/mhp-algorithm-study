class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            // 공백은 그대로 유지
            if (s.charAt(i) == ' ') {
                sb.append(" ");
                continue;
            }

            char c = s.charAt(i);
            int ascii = (int) c;   // 문자를 아스키코드로 변환

            // 대문자 (A=65 ~ Z=90)
            if (ascii <= 90) {
                ascii += n;        // n칸 이동

                if (ascii > 90) {  // Z를 넘으면 A로 순환
                    int remain = ascii - 90;       // Z를 초과한 칸 수
                    ascii = 65;                    // A로 돌아옴
                    ascii += remain - 1;           // 초과한 만큼 이동 (A 포함이므로 -1)
                    sb.append((char) ascii);
                } else {           // Z를 안 넘으면 그대로 추가
                    sb.append((char) ascii);
                }

                // 소문자 (a=97 ~ z=122)
            } else {
                ascii += n;        // n칸 이동

                if (ascii > 122) { // z를 넘으면 a로 순환
                    int remain = ascii - 122;      // z를 초과한 칸 수
                    ascii = 97;                    // a로 돌아옴
                    ascii += remain - 1;           // 초과한 만큼 이동 (a 포함이므로 -1)
                    sb.append((char) ascii);
                } else {           // z를 안 넘으면 그대로 추가
                    sb.append((char) ascii);
                }
            }
        }

        return sb.toString();
    }
}