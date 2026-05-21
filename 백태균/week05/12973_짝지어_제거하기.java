import java.util.*;

class Solution {
    public int solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();  // 스택

        for (char c : s.toCharArray()) {  // char 배열로 변환해서 순회
            if (!stack.isEmpty() && stack.peek() == c) {  // stack이 비어 있지 않고 stack 마지막 요소가 c와 같다는 것은 같은 알파벳 2개가 붙어 있다는 뜻
                stack.pop();  // pop
            } else {  // stack이 비어 있고 stack 마지막 요소가 c와 같지 않다는 것은 같은 알파벳이 아니라는 뜻
                stack.push(c);  // push
            }
        }

        if (stack.isEmpty()) {  // stack이 비어있다는 것은 다 제거했다는 것
            return 1;  // 1 리턴
        } else {  // stack이 비어있지 않다는 것은 다 제거하지 못했다는 것
            return 0;  // 0 리턴
        }
    }
}

//========================================
class Solution {
    public int solution(String s) {
        int top = 0;  // 스택의 맨 위 위치 (다음에 쌓일 인덱스)
        char[] stack = new char[s.length()];  // char 배열을 스택으로 사용

        for (int i=0; i<s.length(); i++) {
            // 스택이 비어있지 않고 맨 위 문자가 현재 문자와 같으면 짝을 발견한거니깐
            if (top > 0 && stack[top-1] == s.charAt(i)) {
                top--;  // pop
            } else {  // 스택이 비어있고 맨 위 문자가 현재 문자와 다르다면 짝을 발견하지 못한거니깐
                stack[top] = s.charAt(i);  // push -> 문자 쌓기
                top++;
            }
        }

        if (top == 0) {  // 스택이 비어있다는 의미
            return 1;
        } else {
            return 0;
        }
    }
}