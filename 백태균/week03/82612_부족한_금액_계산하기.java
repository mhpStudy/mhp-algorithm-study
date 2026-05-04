class Solution {
    public long solution(int price, int money, int count) {

        long total = 0;  // 최종 금액

        for (int i=1; i<=count; i++) {
            total += price * i;  // N배를 구한 값을 최종 금액에 더하기
        }

        if (total - money < 0) {  // 음수이면 금액이 부족하지 않으니깐
            return 0;  // 0 반환
        } else {  // 양수이면 금액이 부족하다는 뜻이니깐
            return total - money;  // 최종 금액에서 현재 가지고 있는 금액을 뺀 값을 반환
        }
    }
}