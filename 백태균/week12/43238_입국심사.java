import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        // N은 연산량이 21억이 넘기 때문에 long을 써야함
        // 1,000,000,000 * 100,000 = 100조 -> int 범위 초과 -> long 사용
        
        Arrays.sort(times);  // 최악의 경우를 구하기 위해 오름차순으로 정렬
        
        long left = 1;
        long right = (long) times[times.length-1] * n;  // 최악의 경우
        long available = right;
        
        // 이분탐색 진행
        while (left <= right) {
            long mid = (left + right) / 2;
            long cnt = 0;
            
            for (int time : times) {
                cnt += mid / time;
                
                // cnt가 n보다 크면 이미 충분하니깐 break 
                if (cnt >= n) {
                    break;
                }
            }
            
            if (cnt >= n) {
                available = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return available;
    }
}