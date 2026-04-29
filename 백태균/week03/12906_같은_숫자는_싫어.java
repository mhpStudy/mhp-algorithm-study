import java.util.*;

public class Solution {
    public int[] solution(int []arr) {

        Deque<Integer> stack = new ArrayDeque<>();  // 스택 선언
        stack.offerLast(arr[0]);  // arr의 첫번째 값을 stack에 추가

        for (int i=1; i<arr.length; i++) {  // arr의 2번째부터 마지막까지 순회하면서
            if (stack.peekLast() != arr[i]) {  // stack의 마지막 값이 다음 추가할 값이랑 같으면 안되기 때문에 다르다면
                stack.offerLast(arr[i]);  // arr[i] 값을 stack에 추가
            }
        }

        return stack.stream().mapToInt(x -> x).toArray();  // stack을 배열로 변환해서 출력
    }
}