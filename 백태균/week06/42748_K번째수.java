import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {

        List<Integer> answer = new ArrayList<>();

        for (int i=0; i<commands.length; i++) {
            int start = commands[i][0] - 1;
            int end = commands[i][1] - 1;
            int outputIndex = commands[i][2] - 1;
            int n = end - start;
            int[] arr = new int[n+1];
            int idx = 0;

            for (int j=start; j<=end; j++) {
                arr[idx] = array[j];
                idx++;
            }

            Arrays.sort(arr);
            answer.add(arr[outputIndex]);
        }

        return answer.stream().mapToInt(x -> x).toArray();
    }
}