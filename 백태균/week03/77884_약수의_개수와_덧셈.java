class Solution {
    public int solution(int left, int right) {
        int answer = 0;

        // left부터 right까지
        for (int i=left; i<=right; i++) {
            int cnt = 0;

            // 1부터 현재 값까지 순회하면서
            for (int j=1; j<=i; j++) {
                // 약수이면
                if (i % j == 0) {
                    cnt++;  // 플러스
                }
            }

            // 약수의 개수가 짝수이면
            if (cnt % 2 == 0) {
                answer += i;  // 해당 값을 더하고
            } else {  // 아니면
                answer -= i;  // 해당 값을 뺴기
            }
        }

        return answer;
    }
}