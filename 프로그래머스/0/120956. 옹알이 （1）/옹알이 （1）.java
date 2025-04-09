class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] words = {"aya", "ye", "woo", "ma"};

        for (String bab : babbling) {
            String w = bab; // ayaye
            for (String word : words) { // "aya", "ye", "woo", "ma"
                if (w.contains(word)) { // ayaye contins aya ?  -> *ye conteins ye ?
                    w = w.replace(word, "*"); // *ye -> **
                }
            }
            w = w.replace("*", ""); // 다시 empty 로 바꿈
            if (w.isEmpty()) {
                answer++;
            }
        }
        return answer;
    }
}