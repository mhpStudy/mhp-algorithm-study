class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];  // 결과 행렬

        // 2차원 배열이니깐 이중 for문 순회
        for (int i=0; i<arr1.length; i++) {
            for (int j=0; j<arr1[0].length; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];  // arr1와 arr2 같은 행, 같은 열의 값을 더한 값을 결과 행렬에 더해서 추가
            }
        }

        return answer;
    }
}