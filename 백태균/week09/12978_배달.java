import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int[][] graph = new int[N+1][N+1];

        for (int i=0; i<=N; i++) {
            for (int j=0; j<=N; j++) {
                if (i == j) {
                    graph[i][j] = 0;
                } else {
                    graph[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        for (int i=0; i<road.length; i++) {
            int start = road[i][0];
            int end = road[i][1];
            int dist = road[i][2];

            graph[start][end] = Math.min(graph[start][end], dist);
            graph[end][start] = Math.min(graph[end][start], dist);
        }

        for (int k=1; k<=N; k++) {
            for (int i=1; i<=N; i++) {
                for (int j=1; j<=N; j++) {
                    if (i == j) {
                        continue;
                    }

                    // Integer.MAX_VALUE + 1 만 해도 오버플로우가 발생하기 때문에 이를 방지
                    if (graph[i][k] == Integer.MAX_VALUE || graph[k][j] == Integer.MAX_VALUE) {
                        continue;
                    }

                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        for (int i=1; i<=N; i++) {
            for (int j=1; j<=N; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }

        int answer = 0;
        for (int i=1; i<=N; i++) {  // 1번 마을에서 출발하는 것만 구하면 됨
            if (graph[1][i] <= K) {
                answer++;
            }
        }

        return answer;
    }
}