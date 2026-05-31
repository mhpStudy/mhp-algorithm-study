import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        // List<Integer> list = new ArrayList<>();
        Set<Integer> set = new HashSet<>();  // Set 사용

        for (int i=0; i<numbers.length-1; i++) {
            int a = numbers[i];

            for (int j=i+1; j<numbers.length; j++) {
                int b = numbers[j];
                int sum = a + b;

                // if (!list.contains(sum)) {
                //     list.add(sum);
                // }

                set.add(sum);
            }
        }

        // int[] answer = new int[list.size()];
        // for (int i=0; i<list.size(); i++) {
        //     answer[i] = list.get(i);
        // }

        int[] answer = new int[set.size()];
        int idx = 0;

        for (int num : set) {
            answer[idx] = num;
            idx++;
        }

        Arrays.sort(answer);

        return answer;
    }
}