import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        // 접근 방법
        // A는 오름차순, B는 내림차순으로 정렬하여
        // A의 작은 값과 B의 큰 값을 순서대로 곱해 합산하면 최솟값을 구할 수 있음

        int answer = 0;

        Arrays.sort(A);  // A 오름차순 정렬
        Arrays.sort(B);  // B 오름차순 정렬 (역방향 인덱스로 내림차순처럼 접근)

        // 순회하면서
        for (int i=0; i<A.length; i++) {
            answer += A[i] * B[B.length-i-1];  // A[i]: 작은 값부터, B[...]: 큰 값부터 곱셈
        }

        return answer;
    }
}