import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        
        // 우선순위 큐를 내림차순으로 생성 (높은 우선순위가 먼저 나오도록)
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        // 모든 우선순위 값을 우선순위 큐에 추가
        for (int num : priorities) {
            pq.add(num);
        }

        // 실행된 프로세스의 개수를 세는 변수
        int cnt = 0;
        
        // 우선순위 큐가 빌 때까지 반복
        while (!pq.isEmpty()) {
            // 원본 배열을 순서대로 확인
            for (int i=0; i<priorities.length; i++) {
                // 현재 위치의 우선순위가 큐의 최고 우선순위와 같은지 확인
                if (pq.peek() == priorities[i]) {
                    // 우선순위 큐에서 최고 우선순위 제거
                    pq.poll();
                    // 실행 횟수 증가
                    cnt++;
                    
                    // 찾고자 하는 위치의 프로세스가 실행되었다면
                    if (i == location) {
                        // 현재까지의 실행 횟수 반환 (몇 번째로 실행되었는지)
                        return cnt;
                    }
                }
            }
        }

        return cnt;
    }
}