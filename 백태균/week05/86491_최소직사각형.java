class Solution {
    public int solution(int[][] sizes) {
        // 명함을 가로 세로 눕혀서 수납할 수 있기 때문에 가로 세로 비교하면서 가로 세로 중 큰 값을 가로로, 작은 값을 세로로 통일
        // maxWidth, maxHeight을 비교하면서 가로에서 제일 큰 값, 세로에서 제일 큰 값을 계속 각각 갱신
        // 최종으로 나온 가로와 세로를 곱한 값이 정답

        int answer = 0;

        int maxWidth = 0;
        int maxHeight = 0;

        for (int i=0; i<sizes.length; i++) {
            int width = sizes[i][0];
            int height = sizes[i][1];
            int temp = 0;

            if (height > width) {
                temp = width;
                width = height;
                height = temp;
            }

            if (width > maxWidth) {
                maxWidth = width;
            }

            if (height > maxHeight) {
                maxHeight = height;
            }
        }

        return maxWidth * maxHeight;
    }
}