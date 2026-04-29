import java.io.*;
import java.util.*;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  // 입력을 한 줄 통째로 버퍼에 담음

        StringTokenizer st = new StringTokenizer(br.readLine());  // 정규식 안쓰고 공백 기준으로 자름
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<m; i++) {  // m개의 * 문자
            for (int j=0; j<n; j++) {  // 줄 개수
                sb.append("*");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}