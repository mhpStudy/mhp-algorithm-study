class Solution {
    public int solution(int[] number) {
        int answer = 0;  // 삼총사 조합의 수

        for (int i=0; i<number.length; i++) {  // 첫 번째 원소 선택 (i)
            for (int j=i+1; j<number.length; j++) {  // 두 번째 원소 선택 (i 다음부터)
                for (int k=j+1; k<number.length; k++) {  // 세 번째 원소 선택 (j 다음부터)

                    // 세 수의 합이 0이면 삼총사 카운트 증가
                    if (number[i] + number[j] + number[k] == 0) {
                        answer++;
                    }
                }
            }
        }

        return answer;
    }
}