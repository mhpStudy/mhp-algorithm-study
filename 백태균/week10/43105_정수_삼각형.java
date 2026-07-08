class Solution {
    public int solution(int[][] triangle) {
        int[][] dp = new int[triangle.length][triangle.length];

        dp[0][0] = triangle[0][0];  // 초기값

        for (int i=1; i<triangle.length; i++) {
            for (int j=0; j<triangle[i].length; j++) {
                if (j == 0) {  // 왼쪽 대각선은 왼쪽 대각선 그대로 더한 값을 dp에 저장
                    dp[i][j] = triangle[i][j] + dp[i-1][j];
                } else if (j == triangle[i].length-1) {  // 오른쪽 대각선도 오른쪽 대각선 그대로 더한 값을 dp에 저장
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1];
                } else {  // 그 외에는 해당 지점에서 왼쪽 아래, 오른쪽 아래 각각 더한 값의 최대값을 dp에 저장
                    dp[i][j] = triangle[i][j] + Math.max(dp[i-1][j-1], dp[i-1][j]);
                }
            }
        }

//         for (int i=0; i<triangle.length; i++) {
//             for (int j=0; j<triangle[i].length; j++) {
//                 System.out.print(dp[i][j] + " ");
//             }
//             System.out.println();
//         }

        int result = 0;
        for (int i=0; i<dp[triangle.length-1].length; i++) {
            result = Math.max(result, dp[triangle.length-1][i]);
        }

        return result;
    }
}