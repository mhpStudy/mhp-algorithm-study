import java.util.*;

class Solution {
    public int[] solution(int m, int n, int h, int w, int[][] drops) {

        // 가로 먼저 탐색 [m][n-w+1]
        // 그 다음 세로 탐색 [m-h+1][n-w+1]

        int[][] arr = new int[m][n];
        for (int i=0; i<m; i++) {
            Arrays.fill(arr[i], Integer.MAX_VALUE);
        }

        int order = 1;
        for (int[] drop : drops) {
            arr[drop[0]][drop[1]] = order;
            order++;
        }

        // 가로 슬라이딩 윈도우 최솟값
        int[][] widthReduce = new int[m][n-w+1];
        for (int i=0; i<m; i++) {
            Deque<Integer> q = new ArrayDeque<>();  // 열 인덱스 저장하는 덱

            for (int j=0; j<n; j++) {
                // 윈도우 왼쪽 경계를 벗어났으면 q의 앞부분 제거
                while (!q.isEmpty() && q.peekFirst() <= j - w) {
                    q.pollFirst();
                }

                // 새 값 arr[i][j] 이상인 뒤쪽 후보 제거
                while (!q.isEmpty() && arr[i][q.peekLast()] >= arr[i][j]) {
                    q.pollLast();
                }

                q.offerLast(j);

                // 윈도우가 처음 꽉 차는 j = w-1 부터 출력. front가 곧 현재 윈도우 최솟값
                if (j >= w - 1) {
                    widthReduce[i][j-w+1] = arr[i][q.peekFirst()];
                }
            }
        }

        // 세로 슬라이딩 최솟값
        int[][] heightReduce = new int[m-h+1][n-w+1];
        for (int j=0; j<n-w+1; j++) {
            Deque<Integer> q = new ArrayDeque<>();

            for (int i=0; i<m; i++) {
                while (!q.isEmpty() && q.peekFirst() <= i - h) {
                    q.pollFirst();
                }

                while (!q.isEmpty() && widthReduce[q.peekLast()][j] >= widthReduce[i][j]) {
                    q.pollLast();
                }

                q.offerLast(i);

                if (i >= h - 1) {
                    heightReduce[i-h+1][j] = widthReduce[q.peekFirst()][j];
                }
            }
        }

        int latest = -1;
        int x = 0;
        int y = 0;

        for (int i=0; i<m-h+1; i++) {
            for (int j=0; j<n-w+1; j++) {
                if (heightReduce[i][j] > latest) {
                    latest = heightReduce[i][j];
                    x = i;
                    y = j;
                }
            }
        }

        return new int[]{x, y};
    }
}