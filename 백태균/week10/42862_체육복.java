import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);

        Set<Integer> set = new HashSet<>();
        boolean[] arr = new boolean[n+1];

        // 전체 체육복이 있다는 것으로 초기화
        for (int i=1; i<=n; i++) {
            arr[i] = true;
        }

        // lost에 있는 값들은 false
        for (int l : lost) {
            arr[l] = false;
        }

        // 체육복을 빌려줄 수 있는 사람들을 set에 추가
        for (int num : reserve) {
            set.add(num);
        }

        /**
         여벌 체육복을 가져온 학생이 체육복을 도난 당했을 때 다른 학생에게는 체육복을 빌려줄 수
         없기 때문에 set에서 제거하고 arr를 true로 변환
         **/
        for (int i=0; i<lost.length; i++) {
            for (int j=0; j<reserve.length; j++) {
                if (lost[i] == reserve[j]) {
                    set.remove(lost[i]);
                    arr[lost[i]] = true;
                    lost[i] = 0;  // lost에서도 이 부분은 그냥 넘겨야하기 때문에 0으로 변환
                }
            }
        }

        for (int l : lost) {
            if (l == 0) {  // 여벌 체육복을 가져온 학생이 체육복을 도난 당한 상황
                continue;
            }

            // set이 비어있으면 체육복을 더 이상 빌려줄 수 없다는 뜻
            if (set.isEmpty()) {
                break;
            }

            // set에 l의 1보다 큰 값이나 작은 값이 있다는 것은 체육복을 빌릴 수 있다는 뜻
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