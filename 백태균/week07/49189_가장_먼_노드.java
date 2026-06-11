import java.util.*;

class Solution {

    static boolean[] visited;
    static int[] dists;
    static List<ArrayList<Integer>> tree;

    public int solution(int n, int[][] edge) {

        visited = new boolean[n+1];
        dists = new int[n+1];  // 1번 노드로부터 각 노드까지의 최단 거리를 저장하는 배열
        tree = new ArrayList<>();  // 그래프를 인접 리스트 형태로 저장

        // list 안에 또 다른 list 추가
        for (int i=0; i<n+1; i++) {
            tree.add(new ArrayList<>());
        }

        // 간선 정보를 바탕으로 양방향 그래프 생성
        for (int[] con : edge) {
            int startNode = con[0];
            int endNode = con[1];

            // 양방향 그래프
            tree.get(startNode).add(endNode);
            tree.get(endNode).add(startNode);
        }

        bfs(1);  // bfs 실행

        int maxDist = 0;  // 가장 먼 거리 값을 저장할 변수

        // 돌면서 가장 큰 거리 찾기
        for (int i=1; i<=n; i++) {
            maxDist = Math.max(maxDist, dists[i]);
        }

        int cnt = 0;

        // 최단 거리가 maxDist와 같은 노드의 개수 찾기
        for (int i=1; i<=n; i++) {
            if (dists[i] == maxDist) {
                cnt++;
            }
        }

        return cnt;
    }

    // 큐에 넣을 노드 정보를 담는 클래스
    static class Pos {
        int node;  // 현재 노드 번호
        int dist;  // 1번 노드로부터 현재 노드까지의 거리

        public Pos(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }

    // BFS 함수
    static void bfs(int startNode) {
        Deque<Pos> q = new ArrayDeque<>();

        // 시작 노드인 1번 노드를 큐에 삽입
        q.offer(new Pos(startNode, 0));
        visited[startNode] = true;

        while (!q.isEmpty()) {
            // 큐에서 현재 노드 정보 꺼내기
            Pos pos = q.poll();
            int node = pos.node;
            int dist = pos.dist;

            // 현재 노드와 연결된 모든 다음 노드 확인
            for (int nextNode : tree.get(node)) {
                if (!visited[nextNode]) {
                    int newDist = dist + 1;
                    dists[nextNode] = newDist;
                    q.offer(new Pos(nextNode, newDist));
                    visited[nextNode] = true;
                }
            }
        }
    }
}