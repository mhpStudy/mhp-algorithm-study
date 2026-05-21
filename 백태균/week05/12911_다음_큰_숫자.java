class Solution {
    public int solution(int n) {

        // n의 이진수에서 1의 개수를 센다
        int oneSum = 0;
        String binary = Integer.toString(n, 2);   // n을 2진수 문자열로 변환

        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                oneSum++;                          // 1의 개수 카운트
            }
        }

        n++;   // n보다 큰 수부터 탐색 시작

        // n+1부터 1씩 늘려가며 1의 개수가 같은 수를 찾는다
        boolean flag = false;
        while (!flag) {
            String newBinary = Integer.toString(n, 2);   // 현재 n을 2진수로 변환
            int cntOne = 0;

            for (int i = 0; i < newBinary.length(); i++) {
                if (newBinary.charAt(i) == '1') {
                    cntOne++;                             // 1의 개수 카운트
                }
            }

            // 1의 개수가 원래 수와 같으면 그게 정답
            if (oneSum == cntOne) {
                return n;
            }

            n++;   // 다음 수 검사
        }

        return 0;   // (도달하지 않는 코드, 컴파일을 위한 반환)
    }
}

//==========================================================//
class Solution {
    public int solution(int n) {
        // Integer.bitCount() : n을 2진수로 변환했을 때 1의 개수를 반환

        int standardOne = Integer.bitCount(n);
        n++;

        while (Integer.bitCount(n) != standardOne) {
            n++;
        }

        return n;
    }
}