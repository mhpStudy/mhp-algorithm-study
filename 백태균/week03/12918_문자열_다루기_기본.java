class Solution {
    public boolean solution(String s) {

        char[] arr = s.toCharArray();  // s index 값들을 저장할 char 배열 선언

        boolean check = false;  // 문자열 길이가 4 혹은 6인지 확인하는 flag

        // 문자열 s의 길이가 4 혹은 6이면 진행해야 하니깐 check = true
        if (s.length() == 4 || s.length() == 6) {
            check = true;
        }

        // 문자열의 길이가 4 혹은 6이 아니면
        if (!check) {
            return false;  // false 리턴
        }

        for (char c : arr) {  // arr 배열을 순회하면서
            int num = c - '0';  // char를 int로 변환

            // 1~9까지의 char을 '0'으로 빼주면 1~9으로 변환되기 때문에(이 외에는 문제에서 해당하는 숫자가 안됨) 0보다 작고 9보다 크면
            if (num < 0 || num > 9) {
                return false;  // false 리턴
            }
        }

        // 여기까지 도달했으면 모두 다 숫자 1~9까지 이루어져 있다는 뜻이기 때문에 true 리턴
        return true;
    }
}