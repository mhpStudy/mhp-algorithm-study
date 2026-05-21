class Solution {
    public int solution(int n) {
        // 투 포인터/슬라이딩 윈도우 풀이
        int left = 1;
        int right = 1;
        int sum = 1;
        int cnt = 0;

        while (left <= n) {
            if (sum == n) {  // 연속한 자연수 합한 값이 n과 같다면
                cnt++;  // 카운트 증가하고
                sum -= left;  // 왼쪽 포인터가 가리키는 값을 빼고
                left++;  // 왼쪽 포인터를 다음 값으로 이동
            } else if (sum < n) {  // 연속한 자연수 합한 값이 n보다 작으면 -> 오른쪽 포인터를 계속 증가시킬 수 있음
                right++;  // 오른쪽 포인터를 증가
                sum += right;  // sum에 값 추가
            } else if (sum > n) {  // 연속한 자연수 합한 값이 n보다 크면 -> 왼쪽 포인터가 가르키고 있는 값을 빼고 증가시켜야함
                sum -= left;  // sum에 현재 왼쪽 포인터가 가르키고 있는 값을 빼고
                left++;  // 왼쪽 포인터를 증가
            }
        }

        return cnt;
    }
}