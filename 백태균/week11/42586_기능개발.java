import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        List<Integer> answer = new ArrayList<>();
        int[] remainProgresses = new int[progresses.length];
        
        for (int i=0; i<progresses.length; i++) {
            remainProgresses[i] = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
        }
        
        int start = remainProgresses[0];
        int cnt = 1;
        for (int i=1; i<=remainProgresses.length; i++) {
            
            if (i == remainProgresses.length) {
                answer.add(cnt);
                break;
            }
            
            if (start >= remainProgresses[i]) {
                cnt++;
            } else {
                answer.add(cnt);
                start = remainProgresses[i];
                cnt = 1;
            }
        }
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}