import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // participant랑 completion을 정렬해서 같이 순회하면서 동일한 인물이 나오지 않으면 완주자 명단에 없는 것이기 때문에 그 사람을 출력

        Arrays.sort(participant);
        Arrays.sort(completion);

        int i = 0;  // 완주자 명단에 없는 선수 인덱스
        for (i=0; i<completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                break;
            }
        }

        return participant[i];
    }
}