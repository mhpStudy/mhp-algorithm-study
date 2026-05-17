import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {

        Arrays.sort(d);  // 작은 순으로 순회하면 가장 많은 경우의 수를 바로 알 수 있어서 오름차순으로 정렬

        int sum = 0;
        int cnt = 0;

        // 순회하면서
        for (int i=0; i<d.length; i++) {
            sum += d[i];  // 하나씩 sum에 더하기

            if (sum <= budget) {  // 여태까지 더한 값이 budget 보다 작거나 같다면
                cnt++;  // cnt 증가
            } else {  // 여태까지 더한 값이 budget 보다 크다면
                break;  // 이제 더 이상 찾을 필요가 없으니깐 정지
            }
        }

        return cnt;
    }
}