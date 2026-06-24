import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> set = new HashSet<>();

        for (String num : phone_book) {
            set.add(num);
        }

        // 각 번호를 하나씩 꺼내 접두사 검사
        for (String num : phone_book) {
            for (int i=1; i<num.length(); i++) {
                String prefix = num.substring(0, i);  // 앞에서 i글자만큼 자른 접두사
                if (set.contains(prefix)) {  // 이 접두사가 다른 번호로 존재하면
                    return false;
                }
            }
        }

        return true;
    }
}