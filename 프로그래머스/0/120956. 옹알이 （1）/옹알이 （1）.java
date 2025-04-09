class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] words = {"aya", "ye", "woo", "ma"};
        for(String bob: babbling){
            String w = bob;
            for(String word: words){
                if(w.contains(word)){
                    w = w.replace(word, "*");
                }
            }
            if(w.contains("*")){
                w = w.replace("*", "");
            }
            if(w.isEmpty()){
                answer += 1;
            }
        }
        
        return answer;
    }
}