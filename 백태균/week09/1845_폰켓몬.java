import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int avaLen = nums.length / 2;

        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        // set 길이가 가져갈 수 있는 폰켓몬 수 보다 크다면 무조건 그 만큼 가져갈 수 있으니깐 avaLen 값 리턴
        if (set.size() >= avaLen) {
            return avaLen;
        } else {  // 작으면 set 길이가 최대로 가져갈 수 있는 종류의 수니깐 set 길이 리턴
            return set.size();
        }
    }
}