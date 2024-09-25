import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    int answer = 0;
    String line = sc.nextLine();
    String[] numbers = line.split(" ");
    for(String number : numbers){
      // 1부터
      int count = 0;
      int num = Integer.parseInt(number);
      for(int i = 1; i <= num; i++){
        if (num % i == 0) {
          count ++;
          if (count > 2){
            break;
          }
        }
      }
      if(count == 2){
        answer ++;
      }
    }

    System.out.println(answer);
    sc.close();
  }
}