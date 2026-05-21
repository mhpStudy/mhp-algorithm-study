class Solution {
    public int solution(int n) {
        // 피보나치 점화식: f(n) = f(n-1) + f(n-2)

        int[] fibo = new int[n+1];

        fibo[0] = 0;  // 0번째를 0으로 지정
        fibo[1] = 1;  // 1번째를 1로 지정

        int i = 2;
        while (i <= n) {
            // f(47)부터는 21억을 넘기 때문에 int 범위를 초과함
            fibo[i] = (fibo[i-1] + fibo[i-2]) % 1234567;  // 그래서 fibo(n) 구한 값을 바로 % 1234567 해서 나머지 값을 저장
            i++;
        }

        return fibo[n];
    }
}