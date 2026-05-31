class Solution {
    public String solution(int[] food) {
        StringBuilder answer = new StringBuilder();
        StringBuilder sb = new StringBuilder();

        for (int i=1; i<food.length; i++) {
            if (food[i] / 2 == 0) {  // 몫이 0인 것은 한 선수밖에 줄 수 없으니깐 패스
                continue;
            }

            int share = food[i] / 2;  // 몫이 줄 수 있는 음식의 개수

            String foodNum = String.valueOf(i);
            String repeated = foodNum.repeat(share);  // 몫 만큼 문자 반복

            sb.append(repeated);  // sb에 추가
            answer.append(repeated);  // answer에 추가
        }

        answer.append("0");  // 중간에 물을 배치해야하기 때문에 0 추가

        sb.reverse();  // 두번째 선수한테도 똑같이 줘야하니깐 앞뒤 바꾸고
        answer.append(sb);  // 정답에 추가

        return answer.toString();

    }
}