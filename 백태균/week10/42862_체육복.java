import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);

        Set<Integer> set = new HashSet<>();
        boolean[] arr = new boolean[n+1];

        for (int i=1; i<=n; i++) {
            arr[i] = true;
        }

        for (int l : lost) {
            arr[l] = false;
        }

        for (int num : reserve) {
            set.add(num);
        }

        for (int i=0; i<lost.length; i++) {
            for (int j=0; j<reserve.length; j++) {
                if (lost[i] == reserve[j]) {
                    set.remove(lost[i]);
                    arr[lost[i]] = true;
                    lost[i] = 0;
                }
            }
        }

        for (int l : lost) {
            if (l == 0) {
                continue;
            }

            if (set.isEmpty()) {
                break;
            }

            if (set.contains(l-1)) {
                set.remove(l-1);
                arr[l] = true;
            } else if (set.contains(l+1)) {
                set.remove(l+1);
                arr[l] = true;
            }
        }

        int answer = 0;
        for (int i=1; i<=n; i++) {
            if (arr[i] == true) {
                answer++;
            }
        }

        return answer;
    }
}