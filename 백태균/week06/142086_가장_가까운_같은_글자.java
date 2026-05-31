import java.util.*;

class Solution {
    public int[] solution(String s) {
        List<Integer> list = new ArrayList<>();
        Map<Character, Integer> map = new HashMap<>();

        for (int i=0; i<s.length(); i++) {
            if (!map.containsKey(s.charAt(i))) {  // map에 해당 키 값이 없으면
                map.put(s.charAt(i), i);  // (알파벳, 인덱스) 추가
                list.add(-1);  // 정답 list에 -1 추가
            } else {  // map에 해당 키 값이 있으면
                int idx = map.get(s.charAt(i));  // 전 알파벳 인덱스 값 추출
                list.add(i - idx);  // 현재 인덱스 값에서 전 인덱스 값을 뺀 값을 정답 list에 추가
                map.put(s.charAt(i), i);  // map에 현재 인덱스 값으로 갱신
            }
        }

        return list.stream().mapToInt(x -> x).toArray();
    }
}