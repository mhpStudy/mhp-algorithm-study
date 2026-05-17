class Solution {
    public int[] solution(int n, int m) {

        int gcd = gcd(n, m);  // 유클리드 호제법으로 최대공약수 계산
        int lcm = (n * m) / gcd ;  // 최소공배수 = 두 수의 곱 / 최대공약수

        return new int[]{gcd, lcm};
    }

    // 유클리드 호제법으로 최대공약수(GCD) 구하기
    // a % b == 0이면 b가 최대공약수, 아니면 (b, a%b)로 범위를 줄여 재귀 호출
    static int gcd(int a, int b) {
        if (a % b == 0) {  // 나누어 떨어지면 나누는 수(b)가 최대공약수
            return b;
        }

        int r = a % b;  // 나머지 계산
        a = b;  // a를 b로 교체
        b = r;  // b를 나머지로 교체
        return gcd(a, b);   // 더 작은 수로 재귀 호출
    }
}