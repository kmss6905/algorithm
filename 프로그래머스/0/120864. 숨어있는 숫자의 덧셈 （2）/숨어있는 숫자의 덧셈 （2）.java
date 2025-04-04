class Solution {
    public int solution(String my_string) {
        // 입력 받은 문자열을 첫번째 글자부터 마지막 글자까지 반복하면서
        // 숫자가 나오는 경우는, 연속된 정수가 될 때 까지 임시로 둔 문자열 변수에 concat
        // 그 외에는 그냥 패스한다.
        // ** 문자열 변수를 어느 시점에 정수로 바꿔야 하는 지
        // ** 시간 복잡도를 낮추기 위해서는 숫자가 아닌 char 등장할 때, 임시로 둔 문자열 변수에 변환해야할 값이 남아 있는 경우에, 정수로 바꾸고 answer 에 추가한다. 
        // 그리고 기존 값이 있던 임시 변수는 초기화 한다 (""로)
        
        
        /**
        
            마지막의 경우를 생각하지 않았음
            마지막에 숫자가 오는 경우에는 tempStrNum 에 남아있다.
            => 따라서 최종 값을 출력하기 전에 남아 있는 지 최종적으로 다시 한번 확인하고 반환한다.
            ex) fjksajeklfjkl123 -> 경우 아마 0이 나올거임..
            
        
        **/
        String tempStrNum = "";
        int answer = 0;
        for(int i = 0; i < my_string.length(); i ++){
            char a = my_string.charAt(i);
            if(Character.isDigit(a)){
                tempStrNum += a;
            }else{
                if(tempStrNum != "") {
                    // System.out.println(tempStrNum);
                    answer += Integer.parseInt(tempStrNum);
                    tempStrNum = "";
                }
            }
        }
        
        if(tempStrNum != ""){
            answer += Integer.parseInt(tempStrNum);
        }
        return answer;
    }
}