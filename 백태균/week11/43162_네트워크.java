import java.util.*;

class Solution {
    
    List<ArrayList<Integer>> graph;
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        graph = new ArrayList<>();
        visited = new boolean[computers.length];
        
        for (int i=0; i<computers.length; i++) {
            graph.add(new ArrayList<>());
        }
        
        // 인접 리스트 구성
        for (int i=0; i<computers.length; i++) {
            for (int j=0; j<computers[0].length; j++) {
                // 자기 자신은 제외
                if (i == j) {
                    continue;
                }
                
                // 1이면 연결되어 있다는 거니깐 인접 리스트에 단방향으로 추가
                if (computers[i][j] == 1) {
                    graph.get(i).add(j);
                }
            }
        }
        
        // 연결된 네트워크 개수 세기
        int cnt = 0;
        for (int i=0; i<computers.length; i++) {
            // 방문하지 않았다는 것은 새로운 네트워크의 시작이라는 뜻
            if (!visited[i]) {
                dfs(i);
                cnt++;
            }
        }
        
        return cnt;
    }
    
    // 얼마나 깊이 연결되어 있는지 확인하기 위해 dfs 사용
    public void dfs(int startNode) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(startNode);
        visited[startNode] = true;
        
        while (!stack.isEmpty()) {
            int node = stack.pop();
            
            for (int nextNode : graph.get(node)) {
                if (!visited[nextNode]) {
                    stack.push(nextNode);
                    visited[nextNode] = true;
                }
            }
        }
    }
}