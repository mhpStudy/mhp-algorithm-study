class Solution {
    public int solution(int n) {

        String trinary = Integer.toString(n, 3);  // 3진수로 변환한 값을 String 변수로 저장
        StringBuilder sb = new StringBuilder(trinary);
        trinary = sb.reverse().toString();  // 앞뒤로 뒤집기

        // trinary는 문자열이기 때문에 컴퓨터는 문자열이 몇 진수인지 구별을 못함
        // 그래서 지금 현재 문자열이 3진수야 라는 것을 알려줘야 하기 때문에 (trinary, 3) 으로 넣고
        // Integer.parseInt()로 10진수 반환
        int decimal = Integer.parseInt(trinary, 3);

        return decimal;
    }
}