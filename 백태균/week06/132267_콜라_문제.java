class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;

        while (n >= a) {  // a 미만이면 콜라를 받을 수 없으니깐
            int div = (n / a) * b;  // 현재 n개를 a만큼 먹고 받을 수 있는 콜라의 수
            int remain = n % a;  // n개를 a만큼 먹고 남은 콜라의 수

            answer += div;
            n = div + remain;  // n을 받은 콜라의 수와 남은 콜라의 수로 갱신
        }

        return answer;
    }
}