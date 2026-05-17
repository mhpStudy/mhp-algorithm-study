import java.util.*;

class Solution {
    public String solution(String s) {

        String[] arr = s.split(" ");  // 문자열 s를 띄어쓰기 기준으로 split해서 String 배열로 변환

        int maxNum = Integer.MIN_VALUE;  // 최대값 저장 배열
        int minNum = Integer.MAX_VALUE;  // 최소값 저장 배열

        for (int i=0; i<arr.length; i++) {
            String c = arr[i];
            int num = Integer.parseInt(c);  // int 타입으로 변환해주고

            if (num > maxNum) {  // 최대값보다 큰 수면 갱신
                maxNum = num;
            }

            if (num < minNum) {  // 최소값보다 작은 수면 갱신
                minNum = num;
            }
        }

        StringBuilder sb = new StringBuilder();  // StringBuilder를 만들어주고
        sb.append(minNum).append(" ").append(maxNum);  // 정답 형식으로 추가

        return sb.toString();  // String 타입으로 바꿔주면서 출력
    }
}