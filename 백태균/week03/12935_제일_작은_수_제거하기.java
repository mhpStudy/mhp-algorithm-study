import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();

        if (arr.length == 1) {  // 숫자가 하나일 때는 작은 수를 제거할 수 없음
            return new int[]{-1};
        }

        int min = arr[0];
        int idx = 0;
        for (int i=1; i<arr.length; i++) {  // 순회하면서 제일 작은 수 찾기
            if (arr[i] < min) {
                min = arr[i];
                idx = i;
            }
        }

        for (int i=0; i<arr.length; i++) {  // 순회하면서 제일 작은 수의 인덱스 값이랑 다르면 추가 안하고 continue
            if (idx == i) {
                continue;
            }

            answer.add(arr[i]);
        }


        return answer.stream().mapToInt(x -> x).toArray();
    }
}