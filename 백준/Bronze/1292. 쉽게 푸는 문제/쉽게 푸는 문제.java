import java.util.Scanner;

public class Main {

  public static int sol() {
    Scanner sc = new Scanner(System.in);
    int[] startend = new int[2];
    int[] answer = new int[1001];
    for (int i = 0; i < 2; i ++){
      startend[i] = sc.nextInt();
    }

    int index = 1;
    boolean flag = false;
    for (int i = 1; i <= 1000; i++) {
      for (int j = 0; j < i; j++) {
        if (index < answer.length) {
          answer[index++] = i;
        }
        if(index > startend[1]){
          flag = true;
          break;
        }
      }
      if (flag){
        break;
      }
    }

    int sum = 0;
    for (int i = startend[0]; i <= startend[1]; i++) {
      sum += answer[i];
    }
    return sum;
  }

  public static void main(String[] args) {
    System.out.println(sol());
  }
}