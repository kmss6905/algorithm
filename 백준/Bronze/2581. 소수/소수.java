import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int m = Integer.parseInt(sc.nextLine());
    int n = Integer.parseInt(sc.nextLine());
    ArrayList<Integer> sosus = new ArrayList<>();

    for (int i = m; i <= n; i++) {
      if (i == 1) continue; // 1은 소수가 아님
      boolean flag = false;
      for (int j = 2; j * j <= i; j++) { // i의 제곱근까지만 검사
        if (i % j == 0) { // j가 i의 약수일 경우
          flag = true;
          break;
        }
      }
      if (!flag) { // 소수일 경우
        sosus.add(i);
      }
    }

    if (sosus.isEmpty()) {
      System.out.println(-1);
    } else {
      int sum = 0;
      for (int i = 0; i < sosus.size(); i++) {
        sum += sosus.get(i);
      }
      System.out.println(sum);
      System.out.println(sosus.get(0));
    }
  }
}
