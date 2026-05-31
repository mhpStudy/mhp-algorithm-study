class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow;

        for (int h=3; h<=total; h++) {  // 가로, 세로 무조건 3이상부터 시작

            int w = total / h;

            if ((w-2) * (h-2) == yellow) {  // 위 아래 두줄, 좌우 두줄을 제거하고 곱한 값이 yellow
                return new int[]{w, h};
            }
        }

        return new int[]{0, 0};
    }
}